#!/usr/bin/env python3

import random
MIN_N = 1
MAX_N = 1000
MIN_MOD = 1
MAX_MOD = 10 ** 9 + 7

for t in range(20):
    fname = f'02_random_{t+1:02}.in'
    with open(fname, 'w') as f:
        N = random.randint(MIN_N, MAX_N)
        MOD = random.randint(MIN_MOD, MAX_MOD)
        f.write(f'{N} {MOD}\n')
