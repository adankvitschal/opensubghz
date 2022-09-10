import sys
import os
import math
import time
import random
import ngspyce
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import utils

simdir = '../simulation/'

#try:
#    plt.axline
#except error:
#    print('Error:{}, please update matplotilb'.format(error))
#    exit()

carrier_frequency = 900e6
tran_endtime = 250 / carrier_frequency
tran_settlingtime = 0
tran_timestep=1/(250*carrier_frequency)

#Prepare plots
#fig, axs = plt.subplots(2)

#Load VCO params and results files
print('Loading circuit parameters CSV')
params = pd.read_csv(simdir+'vco_params.csv')
print(params)

print('Loading circuit results CSV')
results_filename = simdir+'vco_results.csv'
results = pd.read_csv(results_filename)
print(results)

# Read netlist
#print('Loading netlist...')
ngspyce.cmd('set num_threads=16')
ngspyce.cmd('set ngbehavior=hsa')
ngspyce.cmd('set ng_nomodcheck')

try:
    ngspyce.source(simdir+'vco_transfer_tb.spice')
except error:
    print('Circuit failed to load')
    print(error)
    exit()

loop=True
while(loop):

    sim_start = time.time()

    plt.clf()
    plt.suptitle('VCO Analysis')
    plt.xlabel('vtune [V]')
    plt.ylabel('frequency [Hz]')

    if len(sys.argv) > 1:
        loop=False
        arg_index = sys.argv[1]

        if arg_index.isnumeric() == False:
            print('Invalid index: {}'.format(argv[1]))
            exit()

        index = int(arg_index)

        if index < 0 or index > len(vco_params.index):
            print('Index {} is out of range (max: {})'.format(index, len(vco_params.index)))
            exit()

        if results.at[index, 'simtime'] > 0:
            print('Overwriting previous results:');
            print('Power: %.2fmW Gain: %.2fdB IIP3: %.2fdB Noise: %.2fdBm'%( \
                1e3*power_results[i,j,k], \
                gain_results[i,j,k], \
                iip3_results[i,j,k], \
                noise_results[i,j,k]))
    else:
        #Choose a random specimen to simulate
        index=random.randint(0,len(params.index)-1);
        first_index=index
        while results.at[index, 'simtime'] > 0:
            print('index %d already filled, steping to next'%(index))
            index=index+1
            if i>(len(params.index)-1):
                index=0
            if index==first_index:
                print('All points already calculated! exiting...')
                exit()

    resultFileName = 'vco_%d'%(index)
    print('Simulation identifier: ' + resultFileName)

    print('Applying params...')

    def debugAlterparams(**kwargs):
        for key,value in kwargs.items():
            print('ngspice cmd> alterparam {}={}'.format(key,value))
            output = ngspyce.cmd('alterparam {}={}'.format(key,value))
            #print('output: {}'.format(output))
        output = ngspyce.cmd('reset')
        #print('output: {}'.format(output))

    iparams = params.iloc[index].to_dict()
    iparams.pop('Unnamed: 0', None)

    print('Params at %d:'%(index))
    print(iparams)

    debugAlterparams(**iparams)
    #ngspyce.alterparams(**params)

    #output = ngspyce.cmd('show m')
    #print('ngspice show output: {}'.format(output))

    print('Running operating point simulation...')
    ngspyce.cmd('op')
    sim_vbias = ngspyce.vector('bias')[0]
    sim_vcm0 = ngspyce.vector('x2.cm0')[0]
    sim_vin = ngspyce.vector('in')[0]
    sim_vip = ngspyce.vector('ip')[0]
    sim_vqn = ngspyce.vector('qn')[0]
    sim_vqp = ngspyce.vector('qp')[0]
    sim_vm3source = ngspyce.vector('x2.m3source')[0]
    sim_vm4source = ngspyce.vector('x3.m4source')[0]
    sim_ibias = ngspyce.vector('i(v.x2.vsense1)')[0]
    sim_ibranch_a = ngspyce.vector('i(v.x2.vsense2a)')[0]
    sim_ibranch_b = ngspyce.vector('i(v.x2.vsense2b)')[0]
    sim_ind_a_current = ngspyce.vector('i(v.x2.vsense3a)')[0]
    sim_ind_b_current = ngspyce.vector('i(v.x2.vsense3b)')[0]

#    print('Quiescent voltages: I_p {} mV I_n:{}mV Q_p{}mV Q_n{}mV'.format(1e3*sim_vip, 1e3*sim_vin,1e3* sim_vqp, 1e3*sim_vqn))

    print('M1>   vgs={}mV vds={}mV'.format(1e3*(sim_vqp-sim_vcm0), 1e3*(sim_vm4source-sim_vcm0)))
    print('M2>   vgs={}mV vds={}mV'.format(1e3*(sim_vqn-sim_vcm0), 1e3*(sim_vm3source-sim_vcm0)))
    print('M3>   vgs={}mV vds={}mV'.format(1e3*(sim_vin-sim_vm3source), 1e3*(sim_vqp-sim_vm3source)))
    print('M4>   vgs={}mV vds={}mV'.format(1e3*(sim_vip-sim_vm4source), 1e3*(sim_vqn-sim_vm4source)))
    print('M5>   vgs={}mV vds={}mV'.format(1e3*sim_vbias, 1e3*sim_vcm0))
    print('vbias={}mV'.format(1e3*sim_vbias))
    print('ibias={}uA ibranch_a={}uA ibranch_b={}uA'.format(sim_ibias*1e6, sim_ibranch_a*1e6, sim_ibranch_b))
    print('ind_a_current={}uA ind_b_current={}uA'.format(sim_ind_a_current*1e6, sim_ind_b_current*1e6))

    power_result = 1.8*sim_ibias
    print('>> POWER: %.2f mW'%(power_result*1e3))

    vtune_step = 0.2
    vtune_points = np.arange(0.0,1.8+vtune_step,vtune_step)
    amplitude_vec = np.zeros(len(vtune_points))
    mainfreq_vec = np.zeros(len(vtune_points))

    print('Starting sequence of TRAN simulations...')
    simindex = 0;
    minfreq_result = 0
    maxfreq_result = 0
    amplitude_result = 0
    for vtune in vtune_points:
        simindex += 1
        print('Simulation {}/{}: vtune={}mV'.format(simindex, len(vtune_points), 1e3*vtune))

        ngspyce.alterparams(vtune=vtune)

        tran_command = 'tran {} {} {}'.format(tran_timestep, tran_endtime, tran_settlingtime)
        print('Running transient simulation: ' + tran_command)
        start_time = time.time()
        ngspyce.cmd(tran_command)
        end_time = time.time();
        print('SIMTIME: Simulation completed in {}s'.format(end_time-start_time))

        time_vector = ngspyce.vector('time')
        vout_vector = ngspyce.vector('ip') - ngspyce.vector('in')

        #plt.plot(time_vector, vout_vector)
        #plt.show()

        print('Calculating FFT...')
        start_time = time.time()
        sp = np.fft.fft(vout_vector)
        freq = np.fft.fftfreq(time_vector.size, d=tran_timestep)
        end_time = time.time()
        #print('FFT done in {}ms'.format(1e3*(end_time-start_time)))
        amplitudes = (2/time_vector.size)*np.abs(sp)

        #drop negative half
        positive_amplitudes = np.split(amplitudes, 2)[0]
        positive_freq = np.split(freq,2)[0]

        #plt.semilogy(positive_freq, positive_amplitudes)
        #plt.show()
        #exit()

        #Store only first FFT result
        #if simindex==1:
        #    tran_results = np.vstack((time_vector, vout_vector)) 
        #    tran_filename = simdir+resultFileName+'_tran_vin%.0f.npy'%(1e3*ivin)
        #    print('Storing TRAN results to file: {}'.format(tran_filename))
        #    np.save(tran_filename, tran_results)
        #    fft_results = np.vstack((freq, amplitudes))
        #    fft_filename = simdir+resultFileName+'_fft_vin%.0f.npy'%(1e3*ivin)
        #    print('Storing FFT results to file: {}'.format(fft_filename))
        #    np.save(fft_filename, fft_results)

        #Get max peak of fft and store as result
        index_mainfreq = np.argmax(amplitudes)
        mainfreq = freq[index_mainfreq]
        mainfreq_amplitude = amplitudes[index_mainfreq]

        print('Main Frequency: %fMHz Amplitude: %f'%(mainfreq/1e6, mainfreq_amplitude))

        if mainfreq_amplitude > 10e-3:
            if mainfreq < minfreq_result or minfreq_result == 0:
                minfreq_result = mainfreq
            if mainfreq > maxfreq_result:
                maxfreq_result = mainfreq
            if mainfreq_amplitude > amplitude_result:
                amplitude_result = mainfreq_amplitude

        mainfreq_vec[simindex-1] = mainfreq
        amplitude_vec[simindex-1] = mainfreq_amplitude

        print(amplitude_vec)
        print(mainfreq_vec)

    #Show transfer curve
    #plt.plot(vtune_points, amplitude_vec, label='amplitude')
    plt.plot(vtune_points, mainfreq_vec, label='frequency')

    plt.savefig(simdir+'vco%d_transfer.png')

    #Reload, update and results
    results = pd.read_csv(results_filename)
    results.at[index, 'simtime'] = time.time() - sim_start
    results.at[index, 'power'] = power_result
    results.at[index, 'min_freq'] = minfreq_result
    results.at[index, 'max_freq'] = maxfreq_result
    results.at[index, 'max_amplitude'] = amplitude_result

    print(results.iloc(index))

    result.to_csv(results_filename)

plt.show()

