#!/usr/bin/python3.8
import numpy as np
import sys
import pathlib
me = pathlib.Path(__file__)
prob_dir = str(me.parent.parent)
sys.path.append(prob_dir)
from tests.geneWorstNo import gen_powerof2_NO, gen_conway_NO
from main_solution.main import solve
MAX = 3 * 10 ** 5


def write(ind, A):
    fname = f'06_WorstYes_{ind:02}.in'
    with open(fname, 'w') as f:
        f.write(f'{len(A)}\n')
        A_str = ' '.join(map(str, A))
        f.write(f'{A_str}\n')
    return


ind = 0
for gen_func in [gen_powerof2_NO, gen_conway_NO]:
    for _ in range(3):
        for rev in range(2):
            A = gen_func()
            A = np.append(A, np.random.randint(1, MAX + 1))
            assert solve(A) is not None
            if rev:
                A = A[::-1]
            write(ind, A)
            ind += 1
