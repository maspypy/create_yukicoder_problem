#!/usr/local/bin/python3.8
import sys
import pathlib
import numpy as np
import random
me = pathlib.Path(__file__)
prob_dir = str(me.parent.parent)
sys.path.append(prob_dir)
from topdown.main import solve

MAX_N = 10 ** 5
MAX_X = 10 ** 9
MAX_Y = 10 ** 9
MAX_Z = 10 ** 9
MAX_A = 10 ** 9


def write_case(category_name, id, A, X, Y, Z):
    np.random.shuffle(A)
    fname = category_name + '_' + f'{id:02}' + '.in'
    N = len(A)
    A_str = ' '.join(np.asarray(A).astype(str))
    with open(fname, 'w') as f:
        f.write(f'{N} {X} {Y} {Z}\n')
        f.write(A_str + '\n')


def write_all(gens):
    for i, g in enumerate(gens, 2):
        category_name = f'{i:02}_{g.__name__}'  # 02_small など
        for j, (A, X, Y, Z) in enumerate(g):
            write_case(category_name, j, A, X, Y, Z)


def small_yes(n_cases):
    for _ in range(n_cases):
        N = random.randint(1, 10)
        A = [random.randint(1, 30000) for _ in range(N)]
        X, Y, Z = 0, 0, 0
        while True:
            if solve(A, X, Y, Z):
                break
            r = random.randint(0, 2)
            if r == 0:
                X += 1
            elif r == 1:
                Y += 1
            else:
                Z += 1
        while True:
            if X and solve(A, X - 1, Y, Z):
                X -= 1
            elif Y and solve(A, X, Y - 1, Z):
                Y -= 1
            elif Z and solve(A, X, Y, Z - 1):
                Z -= 1
            else:
                break
        yield A, X, Y, Z


def small_no(n_cases):
    for _ in range(n_cases):
        while True:
            A, X, Y, Z = next(small_yes(1))
            if X == Y == Z == 0:
                continue
            break
        while True:
            r = random.randint(0, 2)
            if r == 0 and X > 0:
                X -= 1
            if r == 1 and Y > 0:
                Y -= 1
            if r == 2 and Z > 0:
                Z -= 1
            if not solve(A, X, Y, Z):
                break
        yield A, X, Y, Z


def large_yes(n_cases):
    def gen():
        N = np.random.randint(9 * 10 ** 4, 10 ** 5 + 1)
        while True:
            X_use = np.random.randint(0, int(1.8 * MAX_X // N), N)
            Y_use = np.random.randint(0, int(1.8 * MAX_Y // N), N)
            Z_use = np.random.randint(0, int(1.8 * MAX_Z // N), N)
            X = X_use.sum()
            Y = Y_use.sum()
            Z = Z_use.sum()
            if X <= MAX_X and Y <= MAX_Y and Z <= MAX_Z:
                A = 1000 * X_use + 5000 * Y_use + 10000 * Z_use
                A -= np.random.randint(1, 1000, N)
                if np.any(A <= 0):
                    continue
                return A, X, Y, Z
    for _ in range(n_cases):
        yield gen()


def large_no(n_cases):
    for A, X, Y, Z in large_yes(n_cases):
        A[0] += 1000
        yield A, X, Y, Z


def anti_bottomup(n_cases):
    def gen():
        N = np.random.randint(int(MAX_N * .9), MAX_N + 1)
        N1 = N // 3
        N2 = N // 3
        N3 = N - N1 - N2
        A1 = np.random.randint(1, 3001, N1)
        A2 = np.random.randint(3001, 5000, N2)
        A3 = np.random.randint(5001, 10000, N3)
        A = np.concatenate([A1, A2, A3])
        add = np.random.randint(1, MAX_Z // N, N)
        A += add * 10000
        X = (A1 // 1000 + 1).sum()
        Y = len(A2)
        Z = len(A3) + add.sum()
        return A, X, Y, Z
    for _ in range(n_cases):
        yield gen()


def handmade():
    yield [1], 0, 0, 0
    yield np.ones(MAX_N, np.int64), MAX_N // 3, MAX_N // 3, MAX_N - MAX_N // 3 * 2
    yield np.ones(MAX_N, np.int64), MAX_N // 3, MAX_N // 3, MAX_N - MAX_N // 3 * 2 - 1
    yield np.full(MAX_N, MAX_A, np.int64), MAX_X, MAX_Y, MAX_Z
    yield [1001, 1, 1], 2, 1, 0
    yield [1999, 5001], 2, 0, 1


gens = [small_yes(3), small_no(3), large_yes(5), large_no(5), anti_bottomup(10), handmade()]
write_all(gens)
