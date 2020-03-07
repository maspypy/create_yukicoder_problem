#!/usr/bin/env python3

import random
MIN_MOD = 1000
MAX_MOD = 10 ** 9 + 7

for t in range(1, 10):
    fname = f'01_verysmall_{t+1:02}.in'
    with open(fname, 'w') as f:
        N = t
        MOD = random.randint(MIN_MOD, MAX_MOD)
        f.write(f'{N} {MOD}\n')
