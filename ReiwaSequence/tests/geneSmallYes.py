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
    n = len(A)
    fname = f'02_smallYes_{ind:02}.in'
    with open(fname, 'w') as f:
        f.write(f'{n}\n')
        A_str = ' '.join(map(str, A))
        f.write(f'{A_str}\n')
    return


ind = 0
for n in range(2, 5):
    for _ in range(3):
        while True:
            A = np.random.randint(1, 10**5 + 1, n - 1)
            X = np.random.randint(-1, 2, n - 1)
            x = np.dot(A, X)
            if 0 < x <= MAX:
                break
        A = np.append(A, x)
        assert solve(A) is not None
        write(ind, A)
        ind += 1
