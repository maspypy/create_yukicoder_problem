#!/usr/bin/python3.8
import numpy as np
import sys
import pathlib
import itertools
me = pathlib.Path(__file__)
prob_dir = str(me.parent.parent)
sys.path.append(prob_dir)
from tests.geneWorstNo import gen_conway_NO

MAX = 3 * 10 ** 5


sizes = [100, 1000, 3 * 10**5]


def write(ind, A):
    fname = f'07_large_{ind:02}.in'
    with open(fname, 'w') as f:
        f.write(f'{len(A)}\n')
        A_str = ' '.join(map(str, A))
        f.write(f'{A_str}\n')
    return


def gen_none():
    return np.zeros(0, np.int32)


ind = 0
gen_funcs = [gen_conway_NO, gen_none]
it = itertools.product(sizes, gen_funcs, [True, False], [True, False])
for size, gen_func, rev, unique in it:
    A = np.random.randint(1, MAX + 1, size)
    B = gen_func()
    A[:len(B)] = B
    if rev:
        A = A[::-1]
    if unique:
        A = np.unique(A)
        np.random.shuffle(A)
        assert len(A) > 30
    write(ind, A)
    ind += 1
