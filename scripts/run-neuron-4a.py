import os
# needs to find the x64_86 directory
# prior to neuron import!
os.chdir('../generated')

import json
from time import perf_counter as pc
from neuron import h, gui

import sys
if len(sys.argv) == 2:
    dt = float(sys.argv[1])
else:
    dt = None

h('''
//Author: Etay Hay, 2011
//  Models of Neocortical Layer 5b Pyramidal Cells Capturing a Wide Range of
//  Dendritic and Perisomatic Active Properties
//  (Hay et al., PLoS Computational Biology, 2011) 
//
// A simulation of L5 Pyramidal Cell BAC firing.
//
// Edited by L Landsmeer (2022) to fit into simulation benchmark


//====================== General files and tools =====================
load_file("nrngui.hoc")

//====================== cvode =======================================
objref cvode

cvode = new CVode()
''')

if dt is None:
    h('cvode.active(1)')
else:
    h('cvode.active(0)')
    h.dt = dt

h('''

//=================== creating cell object ===========================
load_file("import3d.hoc")
objref L5PC

strdef morphology_file

morphology_file = "../L5bPyrCellHayEtAl2011/NEURON/morphologies/cell1.asc"

load_file("../L5bPyrCellHayEtAl2011/NEURON/models/L5PCbiophys3.hoc")
load_file("../L5bPyrCellHayEtAl2011/NEURON/models/L5PCtemplate.hoc")
L5PC = new L5PCtemplate(morphology_file)

//=================== settings ================================

strdef experiment_type

experiment_type = "BAC" // 'BAP', 'CaBurst', 'EPSP', or 'BAC'

v_init = -80
BACdt = 5

//somatic pulse settings
squareAmp = 1.9 

//EPSP settings
risetau = 0.5
decaytau = 5
Imax = 0.5

proximalpoint = 400
distalpoint = 620

tstop = 600

if (0==strcmp(experiment_type,"BAP")) {
  somastimamp = squareAmp
  EPSPamp = 0
}
if (0==strcmp(experiment_type,"CaBurst")) {
  somastimamp = 0
  EPSPamp = Imax*3
}
if (0==strcmp(experiment_type,"BAC")) {
  somastimamp = squareAmp
  EPSPamp = Imax
}
if (0==strcmp(experiment_type,"EPSP")) {
  somastimamp = 0
  EPSPamp = Imax
}

//======================== stimulus settings ============================

//Somatic pulse
objref st1
st1 = new IClamp(0.5)
st1.amp = somastimamp
st1.del = 295
st1.dur = 5

L5PC.soma st1

//Dendritic EPSP-like current
objref sl,st2,ns,syn1,con1,isyn, tvec

isyn = new Vector()
tvec = new Vector()
sl = new List()
double siteVec[2]

sl = L5PC.locateSites("apic",distalpoint)

maxdiam = 0
for(i=0;i<sl.count();i+=1){
  dd1 = sl.o[i].x[1]
  dd = L5PC.apic[sl.o[i].x[0]].diam(dd1)
  if (dd > maxdiam) {
    j = i
    maxdiam = dd 
  }
}

siteVec[0] = sl.o[j].x[0]
siteVec[1] = sl.o[j].x[1]

access L5PC.apic[siteVec[0]]

st2 = new IClamp(siteVec[1])
st2.amp = 0

L5PC.apic[siteVec[0]] {
	st2
	
  syn1 = new epsp(siteVec[1])
  syn1.tau0 = risetau       
  syn1.tau1 = decaytau   
  syn1.onset = 295 + BACdt  
  syn1.imax = EPSPamp

	cvode.record(&syn1.i,isyn,tvec)
}

//======================== recording settings ============================
objref vsoma, vdend, recSite, vdend2, isoma

vsoma = new Vector()
access L5PC.soma
cvode.record(&v(0.5),vsoma,tvec)

vdend = new Vector()
access L5PC.apic[siteVec[0]]
cvode.record(&v(siteVec[1]),vdend,tvec)

sl = new List()
sl = L5PC.locateSites("apic",proximalpoint)
maxdiam = 0
for(i=0;i<sl.count();i+=1){
  dd1 = sl.o[i].x[1]
  dd = L5PC.apic[sl.o[i].x[0]].diam(dd1)
  if (dd > maxdiam) {
    j = i
    maxdiam = dd 
  }
}

siteVec[0] = sl.o[j].x[0]
siteVec[1] = sl.o[j].x[1]

access L5PC.apic[siteVec[0]]

recSite = new IClamp(siteVec[1])
recSite.amp = 0

L5PC.apic[siteVec[0]] {
	recSite
}

access L5PC.apic[siteVec[0]]
vdend2 = new Vector()
cvode.record(&v(siteVec[1]),vdend2,tvec)

access L5PC.soma
isoma = new Vector()
cvode.record(&st1.i,isoma,tvec)

//======================= plot settings ============================

objref gV, gI, s

gV = new Graph()
gV.size(280,480,-80,40)
gV.label(0.5,0.95,"V")

gI = new Graph()
gI.size(280,480,-6,6)
gI.label(0.5,0.95,"I")

s = new Shape(L5PC.all)
s.color_list(L5PC.axonal,3)
s.color_list(L5PC.somatic,1)
s.color_list(L5PC.basal,1)
s.color_list(L5PC.apical,1)
s.point_mark(st2,2)
s.point_mark(recSite,3)
s.show(0)

//============================= simulation ================================

init()
''')

t0 = pc()
h('''
run()
''')
t1 = pc()
print(f'Simulation done, took: {t1-t0:.3f}s')
print(t1-t0)
with open(f'../results/runtimes', 'a') as f:
    logline = json.dumps(dict(
        method='neuron',
        version='neuron',
        walltime_s=(t1-t0),
        dt='cvode' if dt is None else dt,
        simtime_ms=600,
        figure='4a',
        ))
    print(logline, file=f)


h('''
vsoma.plot(gV,tvec)
vdend.plot(gV,tvec,2,1)
vdend2.plot(gV,tvec,3,1)
isyn.plot(gI,tvec)
isoma.plot(gI,tvec)
''')
