#!/usr/bin/env python3

import numpy as np
import pandas as pd
import json
import matplotlib.pyplot as plt

df = pd.DataFrame.from_records(map(json.loads, open('./results/runtimes')))

for figure, sub in df.groupby('figure'):
    print(f'# Performance analysis for figure {figure}')
    keys = ['dt']
    for g, sub in sub.groupby(keys):
        if g != 0.025 and g != 'cvode':
            continue
        config = dict(zip(keys, g)) if len(keys) > 1 else {keys[0]: g}
        config_line = ','.join(f'{k}={v}' for k, v in config.items())
        print(f' analysis for {config_line}')
        walltime_s = sub.groupby('version')['walltime_s'].min()
        counts = sub.groupby('version')['walltime_s'].count()
        simtime_s = sub.groupby('version')['simtime_ms'].first() / 1000
        for k, v in sorted(dict(100 * walltime_s / walltime_s.min()).items(), key=lambda x: x[1]):
            v = v - 100
            if np.isclose(v, 0):
                rel = f'(fastest)'
            else:
                rel = f'({v:.3f}% slower)'
            slowdown = walltime_s[k]/simtime_s[k]
            print('   ',
                    k.ljust(20),
                    f'{slowdown:.2f} sim.s/bio.s'.ljust(20),
                    rel.ljust(20),
                    f'{counts[k]} trials'
                    )
    print()
