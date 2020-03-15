#!/usr/local/bin/python3.8
import numpy as np


MAX = 10**9


def gen_YES():
    N = np.random.randint(9 * 10 ** 4, 10 ** 5 + 1)
    while True:
        X_use = np.random.randint(0, 5, N)
        Y_use = np.random.randint(0, 2, N)
        Z_use = np.random.randint(0, int(1.8 * MAX // N), N)
        X = X_use.sum()
        Y = Y_use.sum()
        Z = Z_use.sum()
        if X <= MAX and Y <= MAX and Z <= MAX:
            A = 1000 * X_use + 5000 * Y_use + 10000 * Z_use
            A -= np.random.randint(1, 1000, N)
            if np.any(A <= 0):
                continue
            break
    return A, X, Y, Z


def gen_NO():
    A, X, Y, Z = gen_YES()
    A[0] += 1000
    return A, X, Y, Z


for i in range(15):
    fname = f'07_Biased_YES_{i:02}.in'
    A, X, Y, Z = gen_YES()
    N = len(A)
    with open(fname, 'w') as f:
        f.write(f'{N} {X} {Y} {Z}\n')
        A_str = ' '.join(map(str, A))
        f.write(A_str + '\n')


for i in range(15):
    fname = f'08_Biased_NO_{i:02}.in'
    A, X, Y, Z = gen_NO()
    N = len(A)
    with open(fname, 'w') as f:
        f.write(f'{N} {X} {Y} {Z}\n')
        A_str = ' '.join(map(str, A))
        f.write(A_str + '\n')
