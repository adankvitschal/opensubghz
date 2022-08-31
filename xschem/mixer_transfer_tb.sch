v {xschem version=3.0.0 file_version=1.2 }
G {}
K {}
V {}
S {}
E {}
N -60 100 -30 100 {
lab=lop}
N -60 100 -60 140 {
lab=lop}
N 30 100 60 100 {
lab=lon}
N 60 100 60 140 {
lab=lon}
N -190 -220 -30 -220 {
lab=bias1}
N -30 -220 -30 -100 {
lab=bias1}
N 0 -130 0 -100 {
lab=V18}
N 30 -130 30 -100 {
lab=GND}
N 30 -150 30 -130 {
lab=GND}
N 30 -150 60 -150 {
lab=GND}
N 60 -150 60 -130 {
lab=GND}
N -130 -70 -100 -70 {
lab=inp}
N -100 -70 -100 -20 {
lab=inp}
N -100 30 -100 80 {
lab=inn}
N 190 30 190 60 {
lab=outn}
N 100 30 190 30 {
lab=outn}
N 100 -20 270 -20 {
lab=outp}
N 270 -20 270 60 {
lab=outp}
N -320 -70 -190 -70 {
lab=#net1}
N -320 -70 -320 -60 {
lab=#net1}
N -210 80 -210 100 {
lab=#net2}
N -130 80 -100 80 {
lab=inn}
N -210 80 -190 80 {
lab=#net2}
C {devices/vdd.sym} -230 -310 0 0 {name=l1 lab=V18}
C {devices/gnd.sym} -320 60 0 0 {name=l2 lab=GND}
C {devices/vsource.sym} -320 -30 0 1 {name=VRFp value="dc "'vrfq'" AC 0.5 sin("'vrfq'" \{vin1_amplitude/2\} \{carrier_freq+base_freq\})"}
C {devices/vsource.sym} -60 170 0 0 {name=VLOp value="dc 1.8 sin("'vloq'" "'lo_amp/2'" carrier_freq)"}
C {devices/res.sym} -160 -70 1 0 {name=R2
value=50
footprint=1206
device=resistor
m=1}
C {devices/vsource.sym} 60 170 0 0 {name=VLOn value="dc 0 sin("'vloq'" "'-lo_amp/2'" carrier_freq)"}
C {devices/gnd.sym} 60 200 0 0 {name=l3 lab=GND}
C {devices/gnd.sym} -230 -150 0 0 {name=l4 lab=GND}
C {devices/vdd.sym} 0 -130 0 0 {name=l5 lab=V18}
C {devices/gnd.sym} 60 -130 0 0 {name=l6 lab=GND}
C {sky130_fd_pr/corner.sym} 70 -330 0 0 {name=CORNER only_toplevel=false corner=tt}
C {devices/vsource.sym} -360 -210 0 0 {name=VS value="dc 1.8"}
C {devices/vdd.sym} -360 -240 0 0 {name=l7 lab=V18}
C {devices/gnd.sym} -360 -180 0 0 {name=l8 lab=GND}
C {devices/code.sym} 190 -330 0 0 {name=stimuli
only_toplevel=false
value="
*.control
*tran 10p 5us
*save all
*write tb_gain.raw
*.endc
"}
C {devices/lab_pin.sym} -30 -220 0 1 {name=l9 sig_type=std_logic lab=bias1
}
C {devices/lab_pin.sym} 270 50 0 1 {name=l10 sig_type=std_logic lab=outp}
C {devices/lab_pin.sym} -110 -70 3 1 {name=l11 sig_type=std_logic lab=inp}
C {devices/lab_pin.sym} 190 50 0 0 {name=l12 sig_type=std_logic lab=outn}
C {devices/lab_pin.sym} -110 80 1 1 {name=l13 sig_type=std_logic lab=inn}
C {devices/code.sym} 300 -330 0 0 {name=parameters
only_toplevel=false
value="
.option TRTOL=5
.option SCALE=1e-6

.param carrier_freq=900Meg
.param base_freq=5Meg
.param delta_freq=1Meg
.param vin1_amplitude=10e-3
.param vin2_amplitude=10e-3
.param vrfq=1.2
.param vloq=0.8
.param lo_amp=1.2

.param bias_width=0.75
.param mixer_biasfactor=5
.param mixer_m23width=10
.param mixer_m23fingers=4
.param mixer_m4567width=2
.param mixer_m4567fingers=1
.param mixer_rw=2.85
.param mixer_rl=22.8
"}
C {devices/vsource.sym} -230 -280 0 0 {name=VBP value="dc 1m"}
C {devices/lab_pin.sym} -60 120 2 1 {name=l14 sig_type=std_logic lab=lop}
C {devices/lab_pin.sym} 60 120 2 0 {name=l15 sig_type=std_logic lab=lon}
C {devices/capa.sym} 270 90 0 0 {name=C1
m=1
value=0.1p
footprint=1206
device="ceramic capacitor"}
C {devices/gnd.sym} 270 120 0 0 {name=l19 lab=GND}
C {devices/capa.sym} 190 90 0 0 {name=C2
m=1
value=0.1p
footprint=1206
device="ceramic capacitor"}
C {devices/gnd.sym} 190 120 0 0 {name=l20 lab=GND}
C {devices/vsource.sym} -320 30 0 1 {name=VRFauxp value="dc 0 sin(0 "'vin2_amplitude/2'" \{carrier_freq+base_freq+delta_freq\})"}
C {opensubghz/xschem/mixer_param.sym} 0 10 0 0 {name=X2}
C {devices/gnd.sym} -60 200 0 0 {name=l16 lab=GND}
C {devices/vsource.sym} -210 130 0 1 {name=VRFn value="dc "'vrfq'" AC -0.5 sin("'vrfq'" \{-vin1_amplitude/2\} \{carrier_freq+base_freq\})"}
C {devices/vsource.sym} -210 190 0 1 {name=VRFauxn value="dc 0 sin(0 "'-vin2_amplitude/2'" \{carrier_freq+base_freq+delta_freq\})"}
C {devices/gnd.sym} -210 220 0 0 {name=l17 lab=GND}
C {devices/res.sym} -160 80 1 0 {name=R1
value=50
footprint=1206
device=resistor
m=1}
C {opensubghz/xschem/bias.sym} -230 -200 0 0 {name=X1}
