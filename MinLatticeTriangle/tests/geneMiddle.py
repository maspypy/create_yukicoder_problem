#!/usr/bin/python3.8

import random

for i in range(20):
    N = random.randint(10**4, 10**6)
    fname = f'02_middle_{i:02}.in'
    with open(fname, 'w') as f:
        f.write(f'{N}\n')
