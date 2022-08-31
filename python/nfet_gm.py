import math
import ngspyce
from matplotlib import pyplot as plt
import numpy as np

body_eff_param=1.5
surface_pot=0.5
vs=0
kelvin_temp = 27 + 273.15
vt = kelvin_temp * 8.617e-5;

def n_factor(inv_level):
    inv_factor = math.sqrt(inv_level+1)
    value = 1 + body_eff_param / (2 * math.sqrt(2 * surface_pot + vt*(inv_factor-2+math.log(inv_factor-1))) + vs)
    return value

print('Loading netlist...')
ngspyce.source('../simulation/nfet1v8_params_tb.spice')

w=3
l=0.15
q=w/l;

print('Applying parameters...')
ngspyce.alterparams(channel_width=w, channel_length=l)

fig, axs = plt.subplots(2)

fig.suptitle('NFET 1v8 param extraction (W={}um  L={}um)'.format(round(w,3), round(l,3)))
#axs[0].ticklabel_format(style='sci', axis='x', scilimits=(0,0))
#axs[0].ticklabel_format(style='sci', axis='y', scilimits=(0,0))
axs[1].set_ylim([1e-2, 5e1])

axs[0].set(xlabel='VGS [mV]', ylabel='gm/Id [S/A]')
axs[1].set(xlabel='gm/Id [S/A]', ylabel='Idq [uA]')
#axs[2].set(xlabel='inversion level', ylabel='n')

vgs_step = 0.005
#vdsvalues = [1e-3, 13e-3, 25e-3, 0.05,0.15, 0.3, 0.5, 1.0]
vdsvalues=[300e-3,500e-3, 1]

for vds in vdsvalues:

    print('Simulating for VDS='+str(vds*1e3)+'mV');

    ngspyce.alter('vds', dc=vds)

    ngspyce.cmd('dc vgs 0 1.2 '+str(vgs_step))

    vgs= ngspyce.vector('vg')
    ids = ngspyce.vector('i(vds)')
    ids = -ids;

    gm = np.diff(ids)/vgs_step
#    gm = np.insert(gm, 0, gm[0])
    vgs=vgs[:-1]
    ids=ids[:-1]
    gmid_ratio = gm/ids;

    gmid_max = np.amax(gmid_ratio);
    gmid_max_index = np.where(gmid_ratio == gmid_max)[0][0]
    print('gmid_max_index = {}'.format(gmid_max_index))
    slope_factor = 1/(vt*gmid_max)
    print('gm_max='+str(gmid_max)+', slope_factor='+str(slope_factor))

    #get crossing of gmid_max/2
    absolute_val_array = np.abs(gmid_ratio - (gmid_max/2))
    smallest_difference_index = absolute_val_array.argmin()
    vto = vgs[smallest_difference_index]
    isq = ids[smallest_difference_index]/(10*q)

    print('VTO='+str(vto)+'V ISQ='+str(isq*1e9)+'nA')

    axs[0].plot(vgs*1e3, gmid_ratio, label='VDS='+str(vds*1e3)+'mV')

    # ==================
    # get gmid_ratio feasible range
    absolute_diff_start = np.abs(gmid_ratio[gmid_max_index:] - (gmid_max*0.8))
    absolute_diff_end = np.abs(gmid_ratio[gmid_max_index:] - (gmid_max*0.1))
    gmid_start_index = absolute_diff_start.argmin()+gmid_max_index
    gmid_end_index = absolute_diff_end.argmin()+gmid_max_index
    print('feasible gmid range start='
            + str(gmid_ratio[gmid_start_index])
            + ' end='
            + str(gmid_ratio[gmid_end_index]))

#    print('start index: '+str(gmid_start_index))
#    print('end index: '+str(gmid_end_index))

    feasible_ids=ids[gmid_start_index:gmid_end_index]
    feasible_gmid_ratio=gmid_ratio[gmid_start_index:gmid_end_index]
    feasible_inv_level = pow((2/(feasible_gmid_ratio*slope_factor*vt))-1,2)-1

#    print(feasible_inv_level)

    axs[1].semilogy(feasible_gmid_ratio, 1e6*feasible_inv_level*isq, label='ACM0 VDS={}mV'.format(vds*1e3))
    axs[1].semilogy(feasible_gmid_ratio, 1e6*feasible_ids/q, '--', label='LUT VDS={}mV'.format(vds*1e3))

#   print('@vgs=vt0 if='+str(inv_level[smallest_difference_index]))

    #===============
    # take a look at drain current vs inversion level
#    inv_level = pow((2/(gmid_ratio*slope_factor*vt))-1,2)-1

#    for it in range(3):
#        feasible_n_factor = np.copy(feasible_inv_level)
#        n_vec = np.vectorize(n_factor)
#        feasible_n_factor = n_vec(feasible_n_factor)
#        axs[2].plot(feasible_inv_level, feasible_n_factor)
#    axs[2].plot(feasible_inv_level, feasible_inv_level*2*isq*1e6, '--')
    #apply some n_factor corrections
#        feasible_inv_level = pow((2/(feasible_gmid_ratio*feasible_n_factor*vt))-1,2)-1
#    axs[1].semilogy(feasible_gmid_ratio, 1e6*feasible_inv_level*isq, '.', label='ACM1 VDS={}mV'.format(vds*1e3))


    simdir='../simulation/'

    lutFileName = 'gmid_lut_{}.npy'.format(math.floor(vds*1e3))
    lut = np.c_[feasible_gmid_ratio, feasible_ids/q]
    np.save(simdir+lutFileName, lut)
    print('gmid -> idq')
    print(lut)


axs[0].legend()
axs[1].legend()
#fig.legend(loc="upper right")
plt.show()
