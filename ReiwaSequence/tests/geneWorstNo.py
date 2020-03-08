#!/usr/bin/python3.8
import sys
import numpy as np
import pathlib
me = pathlib.Path(__file__)
prob_dir = str(me.parent.parent)
sys.path.append(prob_dir)
from main_solution.main import solve

MAX = 3 * 10 ** 5

A = np.array([2, 3, 4, 5])
print(solve(4, A))

def gen_powerof2_type_example():
    pass


def gen_conway_type_example():
    conway = np.array([
        132568, 199412, 233119, 250115, 258613,
        262936, 265136, 266256, 266826, 267111,
        267259, 267336, 267376, 267396, 267407,
        267413, 267416, 267418, 267419, 267420], np.int32)
    for n in range(10000):
        if solve_small(20, conway + n) is None:
            print(n)

def solve_small(N, A):
    dp = np.zeros(1 << N, np.int32)
    for i, x in enumerate(A):
        dp[1 << i:1 << (i + 1)] = dp[:1 << i] + x
    counts = np.bincount(dp)
    if np.all(counts < 2):
        return None
    S = np.where(counts >= 2)[0][0]
    I = np.where(dp == S)[0]
    p = I[0]
    q = I[1]
    B = A.copy()
    for i in range(N):
        c = ((p >> i) & 1) - ((q >> i) & 1)
        B[i] *= c
    return B



def write(ind, n, A):
    return
    fname = f'05_WorstYes_{ind:02}.in'
    with open(fname, 'w') as f:
        f.write(f'{n}\n')
        A_str = ' '.join(map(str, A))
        f.write(f'{A_str}\n')
    return
