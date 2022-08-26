import os
import math
import time
import random
import ngspyce
from matplotlib import pyplot as plt
import numpy as np
import utils
import bias_params
import mixer_params

simdir = '../simulation/'

try:
    plt.axline
except error:
    print('Error:{}, please update matplotilb'.format(error))
    exit()

carrier_frequency = 900e6
base_frequency = 5e6
delta_frequency = 1e6
sim_endtime = 50 / base_frequency
sim_settlingtime = 10 / base_frequency
sim_timestep=1/(50*carrier_frequency)

#Prepare plots
#fig, axs = plt.subplots(2)

plt.suptitle('Mixer Linearity Analysis')
plt.xlabel('Pin [dBm]')
plt.ylabel('Pout [dBm]')
#plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
#plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
#axs[0].set(xlabel='time', ylabel='Vout [mV]')
#axs[1].set(xlabel='frequency [Hz]', ylabel='Vout [mV]')
#axs[1].set_xlim([0, 3.5*carrier_frequency])
#axs[0].set(xlabel='Pin [dBm]',ylabel='Pout [dBm]')

i=random.randint(0,mixer_params.i_range);
j=random.randint(0,mixer_params.j_range);

#access power results file
power_results_filename = simdir+'mixer_power.npy'
if os.path.exists(power_results_filename):
    power_results = np.load(power_results_filename)
else:
    power_results = np.zeros((mixer_params.i_range+1,mixer_params.j_range+1))

print('Power results:')
print(power_results)

#access gain
gain_results_filename = simdir+'mixer_gain.npy'
if os.path.exists(gain_results_filename):
    gain_results = np.load(gain_results_filename)
else:
    gain_results = np.zeros((mixer_params.i_range+1,mixer_params.j_range+1))

print('Gain results:')
print(gain_results)

#access iip3 result file
iip3_results_filename = simdir+'mixer_iip3.npy'
if os.path.exists(iip3_results_filename):
    iip3_results = np.load(iip3_results_filename)
else:
    iip3_results = np.zeros((mixer_params.i_range+1,mixer_params.j_range+1))

print('IIP3 results:')
print(iip3_results)

#access noise result file
noise_results_filename = simdir+'mixer_noise.npy'
if os.path.exists(noise_results_filename):
    noise_results = np.load(noise_results_filename)
else:
    noise_results = np.zeros((mixer_params.i_range+1,mixer_params.j_range+1))

print('Noise results:')
print(noise_results)

first_i=i
first_j=j
while power_results[i,j] != 0:
    print('index %02d%02d already exists, steping to next'%(i,j))
    i=i+1
    if i>mixer_params.i_range:
        i=0
        j=j+1
    if i==first_i and j==first_j:
        print('All points already calculated! exiting...')
        exit()

resultFileName = 'mixer_ip3_%02d%02d'%(i,j)

print('Simulation index: ' + resultFileName)

# Read netlist
print('Loading netlist...')
ngspyce.source(simdir+'mixer_transfer_tb.spice')

print('Applying params...')
params = mixer_params.makeNetlistParams(i,j)

def debugAlterparams(**kwargs):
    for key,value in kwargs.items():
        print('ngspice cmd> alterparam {}={}'.format(key,value))
        output = ngspyce.cmd('alterparam {}={}'.format(key,value))
        print('output: {}'.format(output))
    output = ngspyce.cmd('reset')
    print('output: {}'.format(output))

debugAlterparams(**params)
#ngspyce.alterparams(**params)

#output = ngspyce.cmd('show m')
#print('ngspice show output: {}'.format(output))

print('Running operating point simulation...')
ngspyce.cmd('op')
bias_vcm1 = ngspyce.vector('x2.cm1')[0]
bias_vcm2a = ngspyce.vector('x2.cm2a')[0]
bias_vcm2b = ngspyce.vector('x2.cm2b')[0]
bias_voutp = ngspyce.vector('outp')[0]
sim_vloq = ngspyce.vector('lop')[0]
sim_vinq = ngspyce.vector('inp')[0]
sim_vbias = ngspyce.vector('vbias')[0]
sim_ibias = ngspyce.vector('i(v.x2.vscm1)')[0]
sim_ibranch = ngspyce.vector('i(v.x2.vscm2a)')[0]
sim_refcurrent = ngspyce.vector('i(v.x1.vsense)')[0]

print('M1>   vgs={}mV vds={}mV'.format(1e3*sim_vbias, 1e3*bias_vcm1))
print('M2-3> vgs={}mV vds={}mV'.format(1e3*(sim_vinq-bias_vcm1), 1e3*(bias_vcm2a-bias_vcm1)))
print('M4-7> vgs={}mV vds={}mV'.format(1e3*(sim_vloq-bias_vcm2a), 1e3*(bias_voutp-bias_vcm2a)))
print('vbias={}mV'.format(1e3*sim_vbias))
print('ibias={}uA ibranch={}uA'.format(sim_ibias*1e6,sim_ibranch*1e6))
print('ref_current={}uA'.format(1e6*sim_refcurrent))

power = 1.8*sim_ibias
print('>> POWER: %.2f mW'%(power*1e3))

power_results[i,j] = power
np.save(power_results_filename, power_results)

#Run noise analysis
print('Running noise simulation...')
ngspyce.cmd('noise v(outp,outn) vrf dec 10 10 1Meg')
ngspyce.cmd('setplot noise2')
onoise = ngspyce.vector('onoise_total')[0]
#inoise = ngspyce.vector('inoise_total')[0]

totalNoise_dbm = 20 *math.log10(onoise/224e-3)

print('>>Total Noise: onoise={}V / {} dBm'.format(onoise, totalNoise_dbm))

noise_results[i,j] = totalNoise_dbm
np.save(noise_results_filename, noise_results)

#input_amplitudes = [5e-3,10e-3,20e-3,50e-3,100e-3,500e-3]
input_amplitudes = [10e-3, 20e-3, 50e-3, 100e-3]
gain_db_vec = []
inputPower_vec = []
linearResponse_vec = []
cubicResponse_vec = []

for ivin in input_amplitudes:
    print('Simulation for vin={}mV'.format(1e3*ivin))
    ngspyce.alterparams(
        vin1_amplitude=ivin,
        vin2_amplitude=ivin)

    tran_command = 'tran {} {} {}'.format(sim_timestep, sim_endtime, sim_settlingtime)
    print('Running transient simulation: ' + tran_command)
    start_time = time.time()
    ngspyce.cmd(tran_command)
    end_time = time.time();
    print('Simulation completed in {}s'.format(end_time-start_time))

    time_vector = ngspyce.vector('time')
    vout_vector = ngspyce.vector('outp') - ngspyce.vector('outn')

    #axs[0].plot(time_vector, vout_vector*1e3, label='m23w={}um'.format(m23width))

    print('Calculating FFT...')
    start_time = time.time()
    sp = np.fft.fft(vout_vector)
    freq = np.fft.fftfreq(time_vector.size, d=sim_timestep)
    end_time = time.time()
    print('FFT done in {}ms'.format(1e3*(end_time-start_time)))
    amplitudes = (2/time_vector.size)*np.abs(sp)
    #axs[1].semilogy(freq, amplitudes*1e3, label='m23w={}'.format(m23width))

    indexBaseFreq = utils.indexof(freq, base_frequency)
    indexCubicResponse = utils.indexof(freq, base_frequency+2*delta_frequency)

    gain_db = 20*math.log10(amplitudes[indexBaseFreq]/ivin)
    inputPower = 20*math.log10(ivin/224e-3)
    linearResponse = 20*math.log10(amplitudes[indexBaseFreq]/224e-3)
    cubicResponse = 20*math.log10(amplitudes[indexCubicResponse]/224e-3)

    print('>> GAIN: {} dB'.format(gain_db))
    print('input power: {} dBm'.format(inputPower))
    print('linear response: {} dBm'.format(linearResponse))
    print('cubic response: {} dBm'.format(cubicResponse))
    gain_db_vec.append(gain_db)
    inputPower_vec.append(inputPower)
    linearResponse_vec.append(linearResponse)
    cubicResponse_vec.append(cubicResponse)
    #print('index@5MHz:{} freq: {} value:{}'.format(index5M, freq[index5M], amplitudes[index5M]))

#Convert lists to numpy vectors
gain_db_vec = np.array(gain_db_vec)
inputPower_vec = np.array(inputPower_vec)
linearResponse_vec = np.array(linearResponse_vec)
cubicResponse_vec = np.array(cubicResponse_vec)

#Store gain at least amplitude
gain_results[i,j] = gain_db_vec[0]
np.save(gain_results_filename, gain_results)

#Calculate IP3 point
numFitPoints = round(len(inputPower_vec)/2)
if numFitPoints < 2:
   numFitPoints = 2

#old method with varying slope
a1,b1=np.polyfit(inputPower_vec[0:numFitPoints], linearResponse_vec[0:numFitPoints], 1)
print('old method: a1={} b1={}'.format(a1,b1))
b1=np.mean(linearResponse_vec-inputPower_vec)
a1=1
print('new method: a1={} b1={}'.format(a1,b1))
plt.axline((0, b1), (1, a1+b1), linewidth=2, color='r')

a3,b3=np.polyfit(inputPower_vec[0:numFitPoints], cubicResponse_vec[0:numFitPoints], 1)
print('old method: a3={} b3={}'.format(a3,b3))
b3=np.mean(cubicResponse_vec-3*inputPower_vec)
a3=3
print('new method: a3={} b3={}'.format(a3,b3))
plt.axline((0,b3),(1,a3+b3), linewidth=2, color='b')

plt.plot(inputPower_vec, linearResponse_vec, inputPower_vec, cubicResponse_vec)

iip3 = (b3-b1)/(a1-a3)
oip3 = a1*iip3+b1
print('IIP3: {} dBm OIP3: {} dBm'.format(iip3, oip3))

iip3_results[i,j] = iip3
np.save(iip3_results_filename, iip3_results)

#Prepare IP3 plot
#plt.plot(iip3, oip3, 'v', color='r')
plt.axvline(x=iip3, color='black', linestyle='--')
plt.axhline(y=oip3, color="black", linestyle="--")
plt.text(iip3+2, oip3-30, "IIP3=%.2fdBm"%iip3, rotation=90, verticalalignment='center')

#axs[0].legend()
#axs[1].legend()
plt.savefig(simdir+resultFileName+'.png')
plt.show()

