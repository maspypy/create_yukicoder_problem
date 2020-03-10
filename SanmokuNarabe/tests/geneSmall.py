#!/usr/bin/python3.8
import sys
import pathlib
me = pathlib.Path(__file__)
prob_dir = str(me.parent.parent)
sys.path.append(prob_dir)
from maspy_py.main import solve
import random


def write(ind, A):
    n = len(A)
    fname = f'02_small_{ind:02}.in'
    with open(fname, 'w') as f:
        f.write(f'{n}\n')
        A_str = ' '.join(map(str, A))
        f.write(f'{A_str}\n')
    return


def gen_YES():
    while True:
        n = random.randint(5, 15)
        S = ''.join(random.choice('ox-') for _ in range(n))
        if S.count('o') != S.count('x'):
            continue
        if solve(S):
            yield S


def gen_NO():
    while True:
        n = random.randint(5, 15)
        S = ''.join(random.choice('ox-') for _ in range(n))
        if S.count('o') != S.count('x'):
            continue
        if not solve(S):
            yield S


gens = [gen_YES(), gen_NO()]
ind = 0
for g in gens:
    for _ in range(5):
        S = next(g)
        write(ind, S)
        ind += 1
