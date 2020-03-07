#!/usr/bin/env python3

import random
MIN_N = 10 ** 6 - 10 ** 5
MAX_N = 10 ** 6

for t in range(10):
    fname = f'03_large1000000007_{t+1:02}.in'
    with open(fname, 'w') as f:
        N = random.randint(MIN_N, MAX_N)
        MOD = 10 ** 9 + 7
        f.write(f'{N} {MOD}\n')
