v {xschem version=3.0.0 file_version=1.2 }
G {}
K {}
V {}
S {}
E {}
N 3110 -70 3110 -40 {
lab=gnd}
N 3030 -100 3070 -100 {
lab=bias}
N 3110 -210 3200 -210 {
lab=cm1}
N 3020 -210 3110 -210 {
lab=cm1}
N 3110 -210 3110 -190 {
lab=cm1}
N 3200 -230 3200 -210 {
lab=cm1}
N 3020 -230 3020 -210 {
lab=cm1}
N 2960 -370 3050 -370 {
lab=cm2a}
N 2870 -370 2960 -370 {
lab=cm2a}
N 3050 -390 3050 -370 {
lab=cm2a}
N 2870 -390 2870 -370 {
lab=cm2a}
N 2940 -260 2980 -260 {
lab=RFp}
N 3240 -260 3280 -260 {
lab=RFn}
N 3260 -370 3350 -370 {
lab=cm2b}
N 3170 -370 3260 -370 {
lab=cm2b}
N 3350 -390 3350 -370 {
lab=cm2b}
N 3170 -390 3170 -370 {
lab=cm2b}
N 3020 -370 3020 -350 {
lab=cm2a}
N 3200 -370 3200 -350 {
lab=cm2b}
N 3090 -420 3130 -420 {
lab=LOn}
N 3110 -420 3110 -390 {
lab=LOn}
N 2790 -420 2830 -420 {
lab=LOp}
N 2830 -480 2870 -480 {
lab=IFp}
N 3350 -480 3390 -480 {
lab=IFn}
N 2870 -510 2870 -450 {
lab=IFp}
N 3350 -510 3350 -450 {
lab=IFn}
N 2870 -590 2870 -570 {
lab=vdd}
N 2870 -590 3350 -590 {
lab=vdd}
N 3350 -590 3350 -570 {
lab=vdd}
N 3110 -620 3110 -590 {
lab=vdd}
N 3050 -470 3050 -450 {
lab=IFn}
N 3050 -470 3190 -500 {
lab=IFn}
N 3190 -500 3350 -500 {
lab=IFn}
N 3170 -470 3170 -450 {
lab=IFp}
N 3030 -500 3170 -470 {
lab=IFp}
N 2870 -500 3030 -500 {
lab=IFp}
N 3390 -420 3430 -420 {
lab=LOp}
N 3300 -540 3330 -540 {
lab=gnd}
N 2820 -540 2850 -540 {
lab=gnd}
C {devices/ipin.sym} 2790 -420 0 0 {name=p1 lab=LOp
}
C {devices/ipin.sym} 2940 -260 0 0 {name=p2 lab=RFp
}
C {devices/ipin.sym} 3280 -260 0 1 {name=p5 lab=RFn
}
C {devices/ipin.sym} 3110 -390 1 1 {name=p7 lab=LOn
}
C {devices/ipin.sym} 3030 -100 2 1 {name=p8 lab=bias
}
C {devices/iopin.sym} 3110 -40 0 0 {name=p9 lab=gnd}
C {devices/iopin.sym} 3110 -620 0 0 {name=p10 lab=vdd}
C {devices/lab_pin.sym} 3430 -420 0 1 {name=l1 sig_type=std_logic lab=LOp}
C {devices/opin.sym} 2830 -480 0 1 {name=p3 lab=IFp}
C {devices/opin.sym} 3390 -480 0 0 {name=p4 lab=IFn}
C {sky130_fd_pr/nfet3_01v8.sym} 3000 -260 0 0 {name=M2
L=0.15
W=20
body=GND
nf=8
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
C {sky130_fd_pr/nfet3_01v8.sym} 3090 -100 0 0 {name=M1
L=0.15
W=50
body=GND
nf=10
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
C {sky130_fd_pr/nfet3_01v8.sym} 3220 -260 0 1 {name=M3
L=0.15
W=20
body=GND
nf=8
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
C {sky130_fd_pr/nfet3_01v8.sym} 2850 -420 0 0 {name=M4
L=0.15
W=10
body=GND
nf=4
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
C {sky130_fd_pr/nfet3_01v8.sym} 3070 -420 0 1 {name=M5
L=0.15
W=10
body=GND
nf=4
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
C {sky130_fd_pr/nfet3_01v8.sym} 3150 -420 0 0 {name=M6
L=0.15
W=10
body=GND
nf=4
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
C {sky130_fd_pr/nfet3_01v8.sym} 3370 -420 0 1 {name=M7
L=0.15
W=10
body=GND
nf=4
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
C {devices/lab_pin.sym} 3200 -210 2 0 {name=l4 sig_type=std_logic lab=cm1}
C {devices/lab_pin.sym} 3350 -370 2 0 {name=l5 sig_type=std_logic lab=cm2b}
C {devices/lab_pin.sym} 2870 -370 2 1 {name=l6 sig_type=std_logic lab=cm2a}
C {devices/vsource.sym} 3110 -160 0 0 {name=Vscm1 value="dc 0"}
C {devices/vsource.sym} 3200 -320 0 0 {name=Vscm2b value="dc 0"}
C {devices/vsource.sym} 3020 -320 0 0 {name=Vscm2a value="dc 0"}
C {devices/lab_pin.sym} 2820 -540 0 0 {name=l2 sig_type=std_logic lab=gnd}
C {devices/lab_pin.sym} 3300 -540 0 0 {name=l3 sig_type=std_logic lab=gnd}
C {sky130_fd_pr/res_xhigh_po_5p73.sym} 2870 -540 0 0 {name=R1
W=5.73
L=10
model=res_xhigh_po_5p73
spiceprefix=X
mult=1}
C {sky130_fd_pr/res_xhigh_po_5p73.sym} 3350 -540 0 0 {name=R2
W=5.73
L=10
model=res_xhigh_po_5p73
spiceprefix=X
mult=1}
C {sky130_fd_pr/corner.sym} 3550 -640 0 0 {name=CORNER only_toplevel=false corner=tt}
