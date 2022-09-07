# Caravel Analog User

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0) [![CI](https://github.com/efabless/caravel_user_project_analog/actions/workflows/user_project_ci.yml/badge.svg)](https://github.com/efabless/caravel_user_project_analog/actions/workflows/user_project_ci.yml) [![Caravan Build](https://github.com/efabless/caravel_user_project_analog/actions/workflows/caravan_build.yml/badge.svg)](https://github.com/efabless/caravel_user_project_analog/actions/workflows/caravan_build.yml)

---

| :exclamation: Important Note            |
|-----------------------------------------|

This project contains the following Rf building blocks:

* Balanced Gilbert Cell Mixer
* Quadrature Voltage Controlled Oscilator

# Simulations

The design is optimized using python scripts integrated to ngspice shared library. This allows simulatons to be executed automatically in a loop and data to be processes using python scientific libraries. To run the simulations, he following tools need to be installed:
* ngspice compiled with shared libraries
* ignamv/ngspyce python library obtained from https://github.com/ignamv/ngspyce
* xschem and skywater sky130B pdks

The optimization process takes into account different gm/Id ratios for the transistors, all located in the moderate inversion region. To calculate the correct W/L ratios for the design transistors, first a set of Look Up Tables (LUTs) must be built. This is done using a testbench and a python script:
1. Open nfet1v8_params_tb schematic
2. Set netlist directory to the simulation folder in the repository
3. Generate netlist
4. Change directory to /python and run `python nfet_gm.py`

This will save a numpy array to teh simulation directory containing drain currents for each gm/Id ratio, which will be used by other scripts.

The steps to run the mixer simulations are the following:
1. Open mixer_transfer_tb schematic using xschem
2. Set netlist directory to the simulation folder in the repository
3. Generate netlists
4. Run `mixer_transfer.py`

This will run simulations in a endless loop, saving all results to the /simulation directory. The will include:
* An image for each point containing the IIP3 analysis
* Four numpy buffer incrementally written with each point result of power, gain, noise and iip3 results.

Results can be analyzed using the mixer_analyze scripts, wich are currently under development.

---

Refer to [README](docs/source/index.rst) for this sample project documentation. 
