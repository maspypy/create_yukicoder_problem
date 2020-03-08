#!/usr/bin/python3.8
import numpy as np

MAX = 3 * 10 ** 5


def write(ind, n, A):
    fname = f'05_WorstYes_{ind:02}.in'
    with open(fname, 'w') as f:
        f.write(f'{n}\n')
        A_str = ' '.join(map(str, A))
        f.write(f'{A_str}\n')
    return
