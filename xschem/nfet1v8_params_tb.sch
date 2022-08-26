v {xschem version=3.0.0 file_version=1.2 }
G {}
K {}
V {}
S {}
E {}
N -90 80 -90 90 {
lab=GND}
N -90 90 0 90 {
lab=GND}
N 0 90 0 100 {
lab=GND}
N -90 0 -90 20 {
lab=vg}
N -90 0 -40 -0 {
lab=vg}
N -0 90 120 90 {
lab=GND}
N 120 80 120 90 {
lab=GND}
N 120 -60 120 20 {
lab=vd}
N 0 -60 120 -60 {
lab=vd}
N 0 -60 0 -30 {
lab=vd}
N 0 30 -0 90 {
lab=GND}
C {devices/gnd.sym} 0 100 0 0 {name=l1 lab=GND}
C {devices/vsource.sym} -90 50 0 0 {name=Vgs value=1}
C {devices/vsource.sym} 120 50 0 0 {name=Vds value=1}
C {sky130_fd_pr/nfet3_01v8.sym} -20 0 0 0 {name=M1
L=channel_length
W=channel_width
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
C {sky130_fd_pr/corner.sym} 230 -150 0 0 {name=CORNER only_toplevel=false corner=tt}
C {devices/code.sym} 370 -150 0 0 {name=stimuli
only_toplevel=false
value="
*.control
*dc vds 0.1 1.8 0.1 vgs 0.4 1.8 0.2
*plot -I(vds)
*dc vgs 0.4 1.8 0.1 vds 0.1 1.7 0.5
*plot -I(vds)
*save all
*write tb_gain.raw
*.endc
"}
C {devices/lab_pin.sym} 0 -60 0 0 {name=l2 sig_type=std_logic lab=vd}
C {devices/lab_pin.sym} -90 0 0 0 {name=l3 sig_type=std_logic lab=vg}
C {devices/code.sym} 380 20 0 0 {name=params
only_toplevel=false
value="
.param channel_width=3
.param channel_length=0.15
"}
