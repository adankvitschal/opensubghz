import ngspyce
from matplotlib import pyplot as plt
import numpy as np

# Read netlist
ngspyce.source('../../simulation/tb_nfet1v8_params.spice')

plt.suptitle('NFET 1v8 param extraction')
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.ylabel('I_D [A]')
plt.xlabel('VDS [V]')

vgsvalues = [0.5,0.7]

for vgs in vgsvalues:

    ngspyce.alter('vgs', dc=vgs)

    ngspyce.cmd('dc vds 0 1.8 0.01')

    vds= ngspyce.vector('vd')
    ids = ngspyce.vector('i(vds)')

    plt.plot(vds, -ids, label='VGS='+str(vgs))

plt.legend(loc="upper left")
plt.show()
