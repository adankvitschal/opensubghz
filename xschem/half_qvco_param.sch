v {xschem version=3.1.0 file_version=1.2 }
G {}
K {}
V {}
S {}
E {}
N -120 -70 -120 -30 {
lab=m3source}
N 120 -70 120 -30 {
lab=m4source}
N -120 110 -120 130 {
lab=cm0}
N 120 110 120 130 {
lab=cm0}
N -70 260 -40 260 {
lab=bias}
N -190 -100 -160 -100 {
lab=I_n}
N 0 290 0 320 {
lab=gnd}
N 0 130 0 150 {
lab=cm0}
N -120 130 120 130 {
lab=cm0}
N -150 -230 -120 -230 {
lab=Q_p}
N 120 -230 150 -230 {
lab=Q_n}
N 0 -190 0 -160 {
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
N -120 -230 -80 -230 {
lab=Q_p}
N 80 -230 120 -230 {
lab=Q_n}
N 0 210 0 230 {
lab=#net1}
N -120 30 -120 50 {
lab=#net2}
N 120 30 120 50 {
lab=#net3}
N 120 -250 120 -130 {
lab=Q_n}
N -120 -250 -120 -130 {
lab=Q_p}
N 0 -350 0 -330 {
lab=gnd}
N 0 -440 -0 -410 {
lab=vdd}
N -120 -390 -60 -390 {
lab=#net4}
N 60 -390 120 -390 {
lab=#net5}
N 120 -390 120 -310 {
lab=#net5}
N -120 -390 -120 -310 {
lab=#net4}
N -20 -230 20 -230 {
lab=vtune}
N -30 -190 30 -190 {
lab=gnd}
N -0 -250 0 -230 {
lab=vtune}
C {sky130_fd_pr/nfet3_01v8.sym} 100 0 0 0 {name=M1
L=0.15
W="'m12_width'"
body=GND
nf="'m12_fingers'"
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
W="'M12_width'"
body=GND
nf="'m12_fingers'"
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
C {sky130_fd_pr/cap_var_lvt.sym} 50 -230 1 1 {name=C1 model=cap_var_lvt W="'capvar_width'" L="'capvar_length'" VM="'capvar_mult'" spiceprefix=X}
C {sky130_fd_pr/cap_var_lvt.sym} -50 -230 3 0 {name=C2 model=cap_var_lvt W="'capvar_width'" L="'capvar_length'" VM="'capvar_mult'" spiceprefix=X}
C {devices/iopin.sym} 0 -440 0 0 {name=p1 lab=vdd}
C {devices/iopin.sym} 0 320 0 0 {name=p2 lab=gnd}
C {sky130_fd_pr/nfet3_01v8.sym} -20 260 0 0 {name=M5
L=0.15
W="'bias_width*bias_factor'"
body=GND
nf="'bias_factor'"
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
W="'m34_width'"
body=GND
nf="'m34_fingers'"
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
W=m34_width
body=GND
nf=m34_fingers
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
C {devices/ipin.sym} -70 260 0 0 {name=p5 lab=bias}
C {devices/opin.sym} -150 -230 0 1 {name=p6 lab=Q_p}
C {devices/opin.sym} 150 -230 0 0 {name=p7 lab=Q_n}
C {devices/ipin.sym} 190 -100 0 1 {name=p8 lab=I_p}
C {devices/ipin.sym} 0 -250 3 1 {name=p3 lab=vtune}
C {devices/lab_pin.sym} 0 -160 0 0 {name=l1 sig_type=std_logic lab=vdd}
C {devices/vsource.sym} 0 180 0 0 {name=Vsense1 value=0}
C {devices/vsource.sym} -120 80 0 0 {name=Vsense2a value=0}
C {devices/vsource.sym} 120 80 0 0 {name=Vsense2b value=0}
C {devices/lab_pin.sym} -120 130 0 0 {name=l3 sig_type=std_logic lab=cm0}
C {devices/lab_pin.sym} -120 -50 0 0 {name=l3 sig_type=std_logic lab=m3source}
C {devices/lab_pin.sym} 120 -50 0 1 {name=l3 sig_type=std_logic lab=m4source}
C {devices/vsource.sym} 120 -280 0 0 {name=Vsense3b value=0}
C {devices/vsource.sym} -120 -280 0 0 {name=Vsense3a value=0}
C {devices/lab_pin.sym} 0 -330 0 0 {name=l2 sig_type=std_logic lab=gnd}
C {opensubghz/xschem/coil_inductor.sym} 0 -390 2 0 {name=XL1
model=sky130_fd_pr__ind_05_125
spiceprefix=X}
