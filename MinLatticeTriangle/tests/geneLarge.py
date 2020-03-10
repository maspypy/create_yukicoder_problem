#!/usr/bin/python3.8

import random

for i in range(10):
    N = random.randint(10**11, 10**12)
    fname = f'04_large_{i:02}.in'
    with open(fname, 'w') as f:
        f.write(f'{N}\n')
