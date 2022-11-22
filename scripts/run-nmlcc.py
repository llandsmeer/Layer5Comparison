#!/usr/bin/env python3

import os, sys
import importlib.util
import subprocess as sp
from pathlib import Path
from time import perf_counter as pc

ARBOR_BUILD_CATALOGUE = 'arbor-build-catalogue'
nmlcc_root = Path('../generated/nmlcc')


import arbor as A

if len(sys.argv) != 2:
    print('usage:', sys.argv[0], '<4a|4b|5a>')
    exit(1)

FIGURE = sys.argv[1]

HOC_FILE = {
        '4a': 'BAC_firing.hoc',
        '4b': 'Step_current_firing.hoc',
        '5a': 'critical_frequency.hoc'
        }

assert FIGURE in {'4b', '4a', '5a'}

def compile(fn, cat):
    fn = fn.resolve()
    cat = cat.resolve()
    recompile = False
    if fn.exists():
        for src in cat.glob('*.mod'):
            src = Path(src).resolve()
            if src.stat().st_mtime > fn.stat().st_mtime:
                recompile = True
                break
    else:
        recompile = True
    if recompile:
        sp.run(f'arbor-build-catalogue local {cat}', shell=True, check=True)
        os.rename(fn.name, fn)
    return A.load_catalogue(fn)

class recipe(A.recipe):
    def __init__(self):
        A.recipe.__init__(self)
        self.props = A.neuron_cable_properties()
        cat = compile(nmlcc_root / 'local-catalogue.so', nmlcc_root / 'cat')
        self.props.catalogue.extend(cat, 'local_')
        self.cell_to_morph = {'L5PC': 'morphology_L5PC', }
        self.gid_to_cell = ['L5PC', ]
        if FIGURE == '4b':
            self.i_clamps = {'Input_0': (699.999988079071, 2000.0, 0.7929999989997327), }
        elif FIGURE == '4a':
            self.i_clamps = {'Input_0': (295.0, 5.0, 1.9), }
        elif FIGURE == '5a':
            self.i_clamps = {'Input_0': [(250 + i*1000/120, 5, 1.99) for i in range(5)]}
        self.gid_to_inputs = { 0: [("seg_0_frac_0.5", "Input_0"), ], }
        self.gid_to_synapses = { }
        self.gid_to_detectors = { }
        self.gid_to_connections = { }
        self.gid_to_labels = { 0: [(0, 0.5), ], }

    def num_cells(self):
        return 1

    def cell_kind(self, _):
        return A.cell_kind.cable

    def cell_description(self, gid):
        cid = self.gid_to_cell[gid]
        mrf = self.cell_to_morph[cid]
        nml = A.neuroml(f'{nmlcc_root}/mrf/{mrf}.nml').morphology(mrf, allow_spherical_root=True)
        lbl = A.label_dict()
        lbl.append(nml.segments())
        lbl.append(nml.named_segments())
        lbl.append(nml.groups())
        lbl['all'] = '(all)'
        if gid in self.gid_to_labels:
            for seg, frac in self.gid_to_labels[gid]:
                lbl[f'seg_{seg}_frac_{frac}'] = f'(on-components {frac} (segment {seg}))'
        dec = A.load_component(f'{nmlcc_root}/acc/{cid}.acc').component
        dec.discretization(A.cv_policy_every_segment())
        if gid in self.gid_to_inputs:
            for tag, inp in self.gid_to_inputs[gid]:
                x = self.i_clamps[inp]
                if not isinstance(x, list):
                    x = [x]
                for lag, dur, amp in x:
                    dec.place(f'"{tag}"', A.iclamp(lag, dur, amp), f'ic_{inp}@{tag}')
        if gid in self.gid_to_synapses:
            for tag, syn in self.gid_to_synapses[gid]:
                dec.place(f'"{tag}"', A.synapse(syn), f'syn_{syn}@{tag}')
        if gid in self.gid_to_detectors:
            for tag in self.gid_to_detectors[gid]:
                dec.place(f'"{tag}"', A.spike_detector(-40), f'sd@{tag}') # -40 is a phony value!!!
        return A.cable_cell(nml.morphology, dec, lbl)

    def probes(self, _):
        # Example: probe center of the root (likely the soma)
        return [A.cable_probe_membrane_voltage('(location 0 0.5)')]

    def global_properties(self, kind):
        return self.props

    def connections_on(self, gid):
        res = []
        if gid in self.gid_to_connections:
            for src, dec, syn, loc, w, d in self.gid_to_connections[gid]:
                conn = A.connection((src, f'sd@{dec}'), f'syn_{syn}@{loc}', w, d)
                res.append(conn)
        return res

ctx = A.context()
mdl = recipe()
ddc = A.partition_load_balance(mdl, ctx)
sim = A.simulation(mdl, ctx, ddc)
hdl = sim.sample((0, 0), A.regular_schedule(0.1))

print('Running simulation for 1s...')
t0 = pc()
if FIGURE == '4b':
    sim.run(3000, 0.025*5)
else:
    sim.run(600, 0.025*5)
t1 = pc()
print(f'Simulation done, took: {t1-t0:.3f}s')

print('Trying to plot...')

import os
import numpy as np
import matplotlib.pyplot as plt

if False:
    if FIGURE == '4b':
        os.system('sh /home/llandsmeer/repos/opensourcebrain/L5bPyrCellHayEtAl2011/NEURON/models/c')
    elif FIGURE == '4a':
        os.system('sh /home/llandsmeer/repos/opensourcebrain/L5bPyrCellHayEtAl2011/NEURON/models/4a')
    else:
        os.system('sh /home/llandsmeer/repos/opensourcebrain/L5bPyrCellHayEtAl2011/NEURON/models/5a')

    nrn_v = np.loadtxt('/home/llandsmeer/repos/opensourcebrain/L5bPyrCellHayEtAl2011/NEURON/simulationcode/v.dat')
    nrn_t = np.loadtxt('/home/llandsmeer/repos/opensourcebrain/L5bPyrCellHayEtAl2011/NEURON/simulationcode/t.dat')
    plt.plot(nrn_t, nrn_v, color='gray', label='Neuron')

plt.title(f'Comparison figure {FIGURE.upper()} ({HOC_FILE[FIGURE]})')

for data, meta in sim.samples(hdl):
  t = data[:, 0]
  v = data[:, 1]
  plt.plot(t, v, label='Arbor')

plt.legend()
plt.xlabel('Time (ms)')
plt.ylabel('Vsoma (mV)')

if FIGURE == '4a':
    plt.xlim([250, 400])
elif FIGURE == '4b':
    pass
else:
    plt.xlim([200, 400])

# plt.savefig(f'comparison_{FIGURE}.png')
# plt.savefig(f'comparison_{FIGURE}.svg')
plt.show()


