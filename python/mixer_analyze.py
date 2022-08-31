import sys
import os
import math
import random
from matplotlib import pyplot as plt
import numpy as np
import utils
import bias_params
import mixer_params

simdir = '../simulation/'

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

fig, axs = plt.subplots(2,2)
fig.suptitle('Mixer Analysis')
#plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
#plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
#axs[1].set(xlabel='frequency [Hz]', ylabel='Vout [mV]')
#axs[2].set_xlim([0, 3.5*carrier_frequency])
#axs[3].set(xlabel='Pin [dBm]',ylabel='Pout [dBm]')

gmid_points = [3, 5, 10, 15, 21]

def annotate_matplot(ax, filter_vec, results):
    for i in range(len(gmid_points)):
        for j in range(len(gmid_points)):
            if filter_vec[i,j] == 0:
                ax.text(j,i, 'X', ha='center', va='center', color='r')
            else:
                text = ax.text(j, i, results[i,j], \
                    ha="center", va="center", color="w")

axs[0,0].set_title('Power [uW]')
axs[0,0].set(xlabel='TS gm/Id', ylabel='SS gm/Id')
axs[0,0].matshow(power_results)
#axs[0,0].set_xticks(np.arange(len(gmid_points)), labels=gmid_points)
#axs[0,0].set_yticks(np.arange(len(gmid_point)), labels=gmid_points)
annotate_matplot(axs[0,0], power_results, np.around(power_results*1e6))

axs[0,1].set_title('Gain [dB]')
axs[0,1].set(xlabel='TS gm/Id', ylabel='SS gm/Id')
axs[0,1].matshow(gain_results)
annotate_matplot(axs[0,1], power_results, np.around(gain_results, decimals=1))

axs[1,0].set_title('IIP3 [dBm]')
axs[1,0].set(xlabel='TS gm/Id', ylabel='SS gm/Id')
axs[1,0].matshow(iip3_results)
annotate_matplot(axs[1,0], power_results, np.around(iip3_results, decimals=1))

thermal_noise = 1.381e-21 * 290 * 1e6 * 50 #T_0 * K_B * BW * R

#print('Thermal noise: {}W'.format(thermal_noise))

noise_factor = np.zeros((mixer_params.i_range+1, mixer_params.j_range+1))
noise_figure = np.zeros((mixer_params.i_range+1, mixer_params.j_range+1))

for i in range(mixer_params.i_range+1):
    for j in range(mixer_params.j_range+1):
        power_gain = math.pow(10, (gain_results[i,j]/10))
        #print('Power gain: {}'.format(power_gain))
        onoise_power = 1e-3*math.pow(10, noise_results[i,j]/10)
        #print('onoise power: {}W'.format(onoise_power))
        noise_factor[i,j] = 1 + (onoise_power / (power_gain * thermal_noise))
        noise_figure[i,j] = 10*math.log10(noise_factor[i,j])
        #print('Noise factor: {} Noise Figure: {} dB'.format(noise_factor[i,j], noise_figure[i,j]))

#print('Noise factor:')
#print(noise_factor)

print('Noise Figure:')
print(noise_figure)

axs[1,1].set_title('Noise Figure (BW=1MHz) [dB]')
axs[1,1].set(xlabel='TS gm/Id', ylabel='SS gm/Id')
axs[1,1].matshow(noise_figure)
annotate_matplot(axs[1,1], power_results, np.around(noise_figure, decimals=1))

plt.show()

fom_results = np.zeros((mixer_params.i_range+1, mixer_params.j_range+1))
pass_specs = np.zeros((mixer_params.i_range+1, mixer_params.j_range+1))

#Min specs, will x-out the FOM plot
max_power = 1e-3 #W
min_gain = 5 #dB
min_iip3 = 0 #dBm
max_nf = 20 # dB

for i in range(mixer_params.i_range+1):
    for j in range(mixer_params.j_range+1):
        if  power_results[i,j] < max_power \
        and gain_results[i,j] > min_gain \
        and iip3_results[i,j] > min_iip3 \
        and noise_figure[i,j] < max_nf:
            pass_specs[i,j] = 1

        if power_results[i,j]>0:
            iip3_watts = 1e-3*math.pow(10, iip3_results[i,j]/10)
            print('IIP: {} dBm = {} W'.format(iip3_results[i,j], iip3_watts))
            fom_results[i,j] = (gain_results[i,j] * iip3_watts) / (noise_figure[i,j] * power_results[i,j])
        else:
            fom_results[i,j] = 0;

print('FOM results:')
print(fom_results);

fig2, axs = plt.subplots(2)
axs[0].matshow(fom_results)
plt.suptitle('Figure of Merit (FOM)')
annotate_matplot(axs[0], pass_specs, np.around(fom_results, decimals=1))
plt.show()
