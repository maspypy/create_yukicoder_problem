#!/usr/bin/python3.8
import numpy as np
import sys
import pathlib
me = pathlib.Path(__file__)
prob_dir = str(me.parent.parent)
sys.path.append(prob_dir)
from main_solution.main import solve


MAX = 3 * 10 ** 5


def write(ind, A):
    fname = f'02_randomYes_{ind:02}.in'
    with open(fname, 'w') as f:
        n = len(A)
        f.write(f'{n}\n')
        A_str = ' '.join(map(str, A))
        f.write(f'{A_str}\n')
    return


ind = 0
for n in range(5, 20):
    while True:
        A = np.random.randint(1, MAX + 1, n)
        if solve(A) is None:
            continue
        break
    write(ind, A)
    ind += 1
