#Python parameter generator for the QCVO
import os
import math
import numpy as np
import pandas as pd
import bias_params

def indexof(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return idx

simdir = '../simulation/'

gmid_lut=np.load(simdir+'gmid_lut_300.npy')

gmid_points = np.linspace(gmid_lut[0,0], gmid_lut[-1,0], 10)
idq_points = []

for gmid in gmid_points:
    idx=indexof(gmid_lut[:,0], gmid)
    idq_points.append(gmid_lut[idx,1])

idq_points = np.array(idq_points)
print(np.c_[gmid_points,idq_points])

#Circuit constants
ibias = 1e-3
lmin=0.15
wmin=0.42
wmax=500
wmax_nofingers = 20
refCurrent=100e-6

#Intermediate constants
capvar_width=30
capvar_length=100
capvar_mult=1
bias_factor=round(ibias/refCurrent)

#Generate free parameters lists
def bias_width_func(idq):
    wval = round(refCurrent/idq)*lmin
    if wval < wmin: wval=wmin
    if wval > wmax_nofingers: wval=wmax_nofingers
    return wval

def m14width_func(idq):
    wval = round(ibias/(2*idq))*lmin
    if wval < wmin: wval=wmin
    if wval > wmax: wval=wmax
    return wval

def finger_func(width):
    if width > 5:
        #Attempt to make transitors closest to square
        nf=math.ceil(width/math.sqrt(width))
        if width/nf > wmax_nofingers:
            nf = math.ceil(width/wmax_nofingers)
    else:
        nf=1
    return nf

#Build params range
m12_widths = np.array([m14width_func(idq) for idq in idq_points])
m34_widths = np.array([m14width_func(idq) for idq in idq_points])
bias_widths = np.array([bias_width_func(idq) for idq in idq_points])

#eliminate duplicates
m12_widths = np.unique(m12_widths)
m34_widths = np.unique(m34_widths)
bias_widths = np.unique(bias_widths)

m12_fingers = np.array([finger_func(width) for width in m12_widths])
m34_fingers = np.array([finger_func(width) for width in m34_widths])

#Intermediate values

#Build param space
param_space_list = []

for bias_width in bias_widths:
    for m12_width in m12_widths:
        m12_fingers = finger_func(m12_width)
        for m34_width in m34_widths:
            m34_fingers = finger_func(m34_width)
            param_space_list.append([bias_width, bias_factor, m12_width, m12_fingers, m34_width, m34_fingers, capvar_width, capvar_length, capvar_mult])

param_filepath = simdir+'vco_params.csv'
if os.path.exists(param_filepath):
    print('Parameters file already exists, please remove it to generate a new one')
    exit()

params = pd.DataFrame(param_space_list, columns=['bias_width', 'bias_factor', 'm12_width', 'm12_fingers', 'm34_width', 'm34_fingers', 'capvar_width','capvar_length', 'capvar_mult'])

print(params)

params.to_csv(param_filepath)

#Generate null result file
results_filepath = simdir+'vco_results.csv'

if os.path.exists(results_filepath):
    print('Results file already exists, please remove it to generate a new one')
    exit()

results = pd.DataFrame(0, index=np.arange(len(params.index)), columns=['simtime', 'power', 'min_freq', 'max_freq', 'max_aplitude', 'max_voltage', 'start_time', 'amplitude915'])

print(results)

results.to_csv(results_filepath)

