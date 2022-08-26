v {xschem version=3.0.0 file_version=1.2 }
G {}
K {}
V {}
S {}
E {}
N -120 -70 -120 -30 {
lab=#net1}
N 120 -70 120 -30 {
lab=#net2}
N -120 -340 -120 -130 {
lab=Q_p}
N -120 -340 -100 -340 {
lab=Q_p}
N -120 30 -120 50 {
lab=#net3}
N 120 30 120 50 {
lab=#net3}
N -70 100 -40 100 {
lab=bias}
N -190 -100 -160 -100 {
lab=I_n}
N 0 -370 -0 -340 {
lab=vdd}
N 0 130 0 160 {
lab=gnd}
N 120 -340 120 -130 {
lab=Q_n}
N 100 -340 120 -340 {
lab=Q_n}
N -40 -340 40 -340 {
lab=vdd}
N 0 50 0 70 {
lab=#net3}
N -120 50 120 50 {
lab=#net3}
N 0 -250 0 -220 {
lab=vtune}
N -150 -230 -120 -230 {
lab=Q_p}
N 120 -230 150 -230 {
lab=Q_n}
N -40 -220 40 -220 {
lab=vtune}
N -0 -170 0 -140 {
lab=gnd}
N 160 -100 190 -100 {
lab=I_p}
N -80 0 -40 0 {
lab=Q_n}
N -40 0 60 -150 {
lab=Q_n}
N 60 -150 120 -150 {
lab=Q_n}
N 40 0 80 0 {
lab=Q_p}
N -60 -150 40 0 {
lab=Q_p}
N -120 -150 -60 -150 {
lab=Q_p}
N -80 -170 80 -170 {
lab=gnd}
N -120 -230 -80 -230 {
lab=Q_p}
N 80 -230 120 -230 {
lab=Q_n}
C {sky130_fd_pr/nfet3_01v8.sym} 100 0 0 0 {name=M1
L=0.15
W=5
body=GND
nf=1
mult=1
ad="'int((nf+1)/2) * W/nf * 0.29'" 
pd="'2*int((nf+1)/2) * (W/nf + 0.29)'"
as="'int((nf+2)/2) * W/nf * 0.29'" 
ps="'2*int((nf+2)/2) * (W/nf + 0.29)'"
nrd="'0.29 / W'" nrs="'0.29 / W'"
sa=0 sb=0 sd=0
model=nfet_01v8
spiceprefix=X
}
C {sky130_fd_pr/nfet3_01v8.sym} -100 0 0 1 {name=M2
L=0.15
W=5
body=GND
nf=1
mult=1
ad="'int((nf+1)/2) * W/nf * 0.29'" 
pd="'2*int((nf+1)/2) * (W/nf + 0.29)'"
as="'int((nf+2)/2) * W/nf * 0.29'" 
ps="'2*int((nf+2)/2) * (W/nf + 0.29)'"
nrd="'0.29 / W'" nrs="'0.29 / W'"
sa=0 sb=0 sd=0
model=nfet_01v8
spiceprefix=X
}
C {sky130_fd_pr/cap_var_lvt.sym} 80 -200 2 1 {name=C1 model=cap_var_lvt W=30 L=30 VM=1 spiceprefix=X}
C {sky130_fd_pr/cap_var_lvt.sym} -80 -200 2 0 {name=C2 model=cap_var_lvt W=30 L=30 VM=1 spiceprefix=X}
C {devices/ind.sym} -70 -340 1 0 {name=L1
m=1
value=10n
footprint=1206
device=inductor}
C {devices/ind.sym} 70 -340 1 0 {name=L2
m=1
value=10n
footprint=1206
device=inductor}
C {devices/iopin.sym} 0 -370 0 0 {name=p1 lab=vdd}
C {devices/iopin.sym} 0 160 0 0 {name=p2 lab=gnd}
C {sky130_fd_pr/nfet3_01v8.sym} -20 100 0 0 {name=M5
L=0.15
W=50
body=GND
nf=1
mult=1
ad="'int((nf+1)/2) * W/nf * 0.29'" 
pd="'2*int((nf+1)/2) * (W/nf + 0.29)'"
as="'int((nf+2)/2) * W/nf * 0.29'" 
ps="'2*int((nf+2)/2) * (W/nf + 0.29)'"
nrd="'0.29 / W'" nrs="'0.29 / W'"
sa=0 sb=0 sd=0
model=nfet_01v8
spiceprefix=X
}
C {devices/ipin.sym} -190 -100 0 0 {name=p4 lab=I_n}
C {sky130_fd_pr/nfet3_01v8.sym} -140 -100 0 0 {name=M3
L=0.15
W=5
body=GND
nf=1
mult=1
ad="'int((nf+1)/2) * W/nf * 0.29'" 
pd="'2*int((nf+1)/2) * (W/nf + 0.29)'"
as="'int((nf+2)/2) * W/nf * 0.29'" 
ps="'2*int((nf+2)/2) * (W/nf + 0.29)'"
nrd="'0.29 / W'" nrs="'0.29 / W'"
sa=0 sb=0 sd=0
model=nfet_01v8
spiceprefix=X
}
C {sky130_fd_pr/nfet3_01v8.sym} 140 -100 0 1 {name=M4
L=0.15
W=5
body=GND
nf=1
mult=1
ad="'int((nf+1)/2) * W/nf * 0.29'" 
pd="'2*int((nf+1)/2) * (W/nf + 0.29)'"
as="'int((nf+2)/2) * W/nf * 0.29'" 
ps="'2*int((nf+2)/2) * (W/nf + 0.29)'"
nrd="'0.29 / W'" nrs="'0.29 / W'"
sa=0 sb=0 sd=0
model=nfet_01v8
spiceprefix=X
}
C {devices/ipin.sym} -70 100 0 0 {name=p5 lab=bias}
C {devices/opin.sym} -150 -230 0 1 {name=p6 lab=Q_p}
C {devices/opin.sym} 150 -230 0 0 {name=p7 lab=Q_n}
C {devices/ipin.sym} 190 -100 0 1 {name=p8 lab=I_p}
C {devices/ipin.sym} 0 -250 3 1 {name=p3 lab=vtune}
C {devices/lab_pin.sym} 0 -140 0 0 {name=l1 sig_type=std_logic lab=vdd}
