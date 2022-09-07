v {xschem version=3.0.0 file_version=1.2 }
G {}
K {}
V {}
S {}
E {}
N -60 -20 -60 20 {
lab=mixer_b1}
N -60 0 -0 0 {
lab=mixer_b1}
N -20 110 20 110 {
lab=mixer_b1}
N -60 -100 -60 -80 {
lab=vdd}
N -60 140 -60 160 {
lab=gnd}
N -0 0 0 50 {
lab=mixer_b1}
N -0 50 0 110 {
lab=mixer_b1}
N -60 160 -60 170 {
lab=gnd}
C {sky130_fd_pr/nfet3_01v8.sym} -40 110 0 1 {name=M1
L=0.15
W=bias_width
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
C {devices/iopin.sym} -60 -100 0 0 {name=p1 lab=vdd}
C {devices/opin.sym} 20 110 0 0 {name=p3 lab=mixer_b1}
C {devices/vsource.sym} -60 50 0 0 {name=Vsense value=0}
C {devices/iopin.sym} -60 170 0 0 {name=p4 lab=gnd}
C {devices/isource.sym} -60 -50 0 0 {name=I0 value=100u}
