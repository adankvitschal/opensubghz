v {xschem version=3.1.0 file_version=1.2 }
G {}
K {}
V {}
S {}
E {}
N -30 -200 -30 -150 {
lab=V18}
N -30 -200 240 -200 {
lab=V18}
N 240 -200 240 -150 {
lab=V18}
N 0 -190 -0 -150 {
lab=GND}
N -0 -190 270 -190 {
lab=GND}
N 270 -190 270 -150 {
lab=GND}
N 30 -180 30 -150 {
lab=bias}
N 30 -180 300 -180 {
lab=bias}
N 300 -180 300 -150 {
lab=bias}
N -100 -350 30 -350 {
lab=bias}
N 30 -350 30 -180 {
lab=bias}
N -30 -400 -30 -200 {
lab=V18}
N -140 -400 -30 -400 {
lab=V18}
N -140 -400 -140 -380 {
lab=V18}
N -140 -280 -140 -250 {
lab=GND}
N -140 -250 -0 -250 {
lab=GND}
N -0 -250 0 -190 {
lab=GND}
N -200 -20 -100 -20 {
lab=ip}
N -200 -20 -200 180 {
lab=ip}
N -200 180 470 180 {
lab=ip}
N 470 -20 470 180 {
lab=ip}
N 370 -20 470 -20 {
lab=ip}
N -170 40 -100 40 {
lab=in}
N -170 40 -170 160 {
lab=in}
N -170 160 450 160 {
lab=in}
N 450 40 450 160 {
lab=in}
N 370 40 450 40 {
lab=in}
N 0 140 270 140 {
lab=#net1}
N 140 140 140 220 {
lab=#net1}
N 100 40 120 40 {
lab=qn}
N 120 40 150 -20 {
lab=qn}
N 150 -20 170 -20 {
lab=qn}
N 120 -20 150 40 {
lab=qp}
N 100 -20 120 -20 {
lab=qp}
N 150 40 170 40 {
lab=qp}
C {devices/vsource.sym} -190 -140 0 0 {name=Vs value=1.8}
C {devices/vsource.sym} 140 250 0 0 {name=Vin value="dc 'vtune'"}
C {devices/gnd.sym} -190 -110 0 0 {name=l1 lab=GND}
C {devices/gnd.sym} 140 280 0 0 {name=l2 lab=GND}
C {devices/gnd.sym} -140 -250 0 0 {name=l3 lab=GND}
C {devices/vdd.sym} -190 -170 0 0 {name=l4 lab=V18}
C {devices/vdd.sym} -140 -400 0 0 {name=l5 lab=V18}
C {sky130_fd_pr/corner.sym} 160 -360 0 0 {name=CORNER only_toplevel=false corner=tt}
C {devices/code.sym} 300 -360 0 0 {name=params only_toplevel=false value="
.param bias_width=10
.param bias_factor=10
.param m12_width=10
.param m12_fingers=2
.param m34_width=10
.param m34_fingers=2
.param capvar_width=30
.param capvar_length=30
.param capvar_mult=4
.param osc_ind=30n

.param vtune = 1
"}
C {devices/lab_pin.sym} 120 -20 3 1 {name=l6 sig_type=std_logic lab=qp}
C {devices/lab_pin.sym} 120 40 3 0 {name=l7 sig_type=std_logic lab=qn}
C {devices/lab_pin.sym} -150 40 1 1 {name=l8 sig_type=std_logic lab=in}
C {devices/lab_pin.sym} -150 -20 3 1 {name=l9 sig_type=std_logic lab=ip}
C {devices/lab_pin.sym} 30 -350 0 1 {name=l10 sig_type=std_logic lab=bias}
C {opensubghz/xschem/bias.sym} -140 -330 0 0 {name=X1}
C {opensubghz/xschem/half_qvco_param.sym} 0 10 0 0 {name=X2}
C {opensubghz/xschem/half_qvco_param.sym} 270 10 0 0 {name=X3}
C {devices/code.sym} 440 -360 0 0 {name=ind_model only_toplevel=false value="

.subckt  sky130_fd_pr__ind_03_90 a b ct sub
R31 net27 b r='1e-2'
R26 a net23 r='1e-2'
C24 net35 net27 c='8.337e-15'
C25 net23 net37 c='53.8e-15'
C0 net27 net31 c='53.8e-15'
R1 sub net31 r='21.56'
R13 net23 net35 r='50.11'
R10 sub net37 r='21.56'
R0 net41 net27 r='1.019'
R9 net23 net39 r='1.019'
    L0 ct net41 l=760.5e-12
    L1 net39 ct l=760.5e-12
.ends sky130_fd_pr__ind_03_90

.subckt  sky130_fd_pr__ind_05_125 a b ct sub
R31 net27 b r='1e-2'
R26 a net23 r='1e-2'
C24 net35 net27 c='103.1e-15'
C25 net23 net37 c='357e-15'
C1 net27 net31 c='357e-15'
R3 sub net31 r='3.67e3'
R2 net41 net27 r='1.7645'
R13 net23 net35 r='9.312'
R10 sub net37 r='3.67e3'
R9 net23 net39 r='1.7645'
    L1 net39 ct l=2.895e-9
    L2 ct net41 l=2.895e-9
.ends sky130_fd_pr__ind_05_125
"}
