#!/usr/bin/python3.8
import sys
import numpy as np
import pathlib
me = pathlib.Path(__file__)
prob_dir = str(me.parent.parent)
sys.path.append(prob_dir)
from main_solution.main import solve

MAX = 3 * 10 ** 5


def gen_powerof2_NO():
    A = np.empty(19, np.int32)
    for i in range(19):
        x = 1 << i
        n = np.random.randint(0, (MAX - x) // (x + x) + 1)
        A[i] = x * (n + n + 1)
    np.random.shuffle(A)
    return A


def gen_conway_NO():
    conway = np.array([
        132568, 199412, 233119, 250115, 258613,
        262936, 265136, 266256, 266826, 267111,
        267259, 267336, 267376, 267396, 267407,
        267413, 267416, 267418, 267419, 267420], np.int32)
    while True:
        n = np.random.randint(0, MAX - conway[-1] + 1)
        if solve(conway + n) is None:
            A = conway + n
            np.random.shuffle(A)
            return A


def write(ind, A):
    fname = f'06_WorstNo_{ind:02}.in'
    with open(fname, 'w') as f:
        f.write(f'{len(A)}\n')
        A_str = ' '.join(map(str, A))
        f.write(f'{A_str}\n')
    return


ind = 0

for _ in range(5):
    A = gen_powerof2_NO()
    assert solve(A) is None
    write(ind, A)
    ind += 1

for _ in range(5):
    A = gen_conway_NO()
    assert solve(A) is None
    write(ind, A)
    ind += 1
