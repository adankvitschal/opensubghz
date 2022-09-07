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

i=0
j=0
k=0
if len(sys.argv) > 1:
    indices_arg = sys.argv[1]
    i = int(indices_arg[0] + indices_arg[1])
    j = int(indices_arg[2] + indices_arg[3])
    k = int(indices_arg[4] + indices_arg[5])
else:
    print('Missing sim index in IIJJKK format')
    exit()

fft_results = np.load(simdir+'mixer_%02d%02d%02d_fft_vin10.npy'%(i,j,k))

print('fft_results dimensios: {}'.format(fft_results.shape))

freq = fft_results[0,:]
amplitudes = fft_results[1,:]
carrier_freq = 900e6

fig, axs = plt.subplots(2)

axs[0].semilogy(freq, amplitudes)
axs[0].set_xlim(0, 3.5*carrier_freq)

tran_results = np.load(simdir+'mixer_%02d%02d%02d_tran_vin10.npy'%(i,j,k))
time = tran_results[0,:]
vout = tran_results[1,:]

axs[1].plot(time, vout)

plt.suptitle('Mixer 2-tone analysis (f1=905Mhz, f2=906MHz)')
plt.show()
