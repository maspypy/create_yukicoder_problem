#!/usr/bin/python3.8

for N in range(1, 20):
    fname = f'01_small_{N:02}.in'
    with open(fname, 'w') as f:
        f.write(f'{N}\n')
