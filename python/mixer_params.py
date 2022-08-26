#Python parameter generator for the gilbert cell mixer
import math
import numpy as np
#import ngspyce
from matplotlib import pyplot as plt
import bias_params

def indexof(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return idx

simdir = '../simulation/'

gmid_lut=np.load(simdir+'gmid_lut_300.npy')

only_gmid = gmid_lut[:,0]

#print(gmid_lut)

gmid_points = np.linspace(gmid_lut[0,0], gmid_lut[-1,0], 5)
idq_points = []

for gmid in gmid_points:
    idx=indexof(gmid_lut[:,0], gmid)
    idq_points.append(gmid_lut[idx,1])

idq_points = np.array(idq_points)
print(np.c_[gmid_points,idq_points])

#Circuit constants
ibias = 500e-6
lmin=0.15
wmin=0.15
wmax=100
rw=5.73
rsquare=300
refCurrent=48e-6

#Intermediate constants
biasfactor=round(ibias/refCurrent)

#Generate free parameters lists
#ibias = np.linspace(500e-6,2e-3, 4)
def m23width_func(idq):
    wval = round(ibias/(2*idq))*lmin
    if wval < wmin: wval=wmin
    if wval > wmax: wval=wmax
    return wval


def m4567width_func(idq):
    wval=round(ibias/(4*idq))*lmin
    if(wval<wmin):wval=wmin
    if(wval>wmax):wval=wmax
    return wval

def m27finger_func(width):
    nf=math.ceil(width/6)
    return nf

m23_widths = np.array([m23width_func(idq) for idq in idq_points])
m4567_widths = np.array([m4567width_func(idq) for idq in idq_points])

m23_fingers = np.array([m27finger_func(width) for width in m23_widths])
m4567_fingers = np.array([m27finger_func(width) for width in m4567_widths])

i_range = m23_widths.size-1
j_range = m4567_widths.size-1

#Intermediate values
drainResistor = 0.6/(ibias/2)

#Dependent params
rl = round((drainResistor/rsquare)*(rw/lmin))*lmin

def makeNetlistParams(i,j):
    print('M1 width: %d x %.2fum'%(biasfactor, bias_params.refCurrentWidth))
    print('M2/M3 width: %d x %.2fum'%(m23_fingers[i], m23_widths[i]/m23_fingers[i]))
    print('M4/M5/M6/M7 width: %d x %.2fum'%(m4567_fingers[j], m4567_widths[j]/m4567_fingers[j]))
    print('Resistor W=%.2fum L=%.2fum R=%.0f Ohms'%(rw, rl, rsquare*rl/rw))
    return {
        'mixer_biasfactor': biasfactor,
        'mixer_m23width': m23_widths[i],
        'mixer_m23fingers': m23_fingers[i],
        'mixer_m4567width': m4567_widths[j],
        'mixer_m4567fingers': m4567_fingers[j],
        'mixer_rl': rl}

