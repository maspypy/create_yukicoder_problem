#!/usr/bin/python3.8
import numpy as np
import sys
import pathlib
me = pathlib.Path(__file__)
prob_dir = str(me.parent.parent)
sys.path.append(prob_dir)
from main_solution.main import solve

MAX = 3 * 10 ** 5


def write(ind, n, A):
    fname = f'04_randomNo_{ind:02}.in'
    with open(fname, 'w') as f:
        f.write(f'{n}\n')
        A_str = ' '.join(map(str, A))
        f.write(f'{A_str}\n')
    return


ind = 0
for n in range(1, 16):
    while True:
        A = np.random.randint(1, MAX + 1, n)
        if solve(n, A) is not None:
            continue
        break
    write(ind, n, A)
    ind += 1
