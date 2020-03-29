#!/usr/local/bin/python3.8
import numpy as np
import sys
import pathlib
me = pathlib.Path(__file__)
prob_dir = str(me.parent.parent)
sys.path.append(prob_dir)
from main_solution.main import solve
MAX = 150000


def check(A):
    """True if solution exists"""
    return solve(A) is not None


def write_case(category_name, id, A):
    fname = category_name + '_' + f'{id:02}' + '.in'
    with open(fname, 'w') as f:
        f.write(f'{len(A)}\n')
        A_str = ' '.join(map(str, A))
        f.write(f'{A_str}\n')


def write_all(gens):
    for i, g in enumerate(gens, 2):
        category_name = f'{i:02}_{g.__name__}'  # 02_small など
        for j, N in enumerate(g):
            write_case(category_name, j, N)


def get_conway(L):
    A = np.array([0, 1, 2, 4, 7, 13, 24, 44, 84, 161, 309, 594, 1164, 2284, 4484, 8807, 17305, 34301, 68008, 134852, 267420], np.int32)
    return A[L] - A[:L][::-1]


def small_yes(n_cases):
    for _ in range(n_cases):
        size = np.random.randint(1, 4)
        while True:
            A = np.random.randint(1, 10**5 + 1, size)
            X = np.random.randint(-1, 2, size)
            x = np.dot(A, X)
            if not (0 < x <= MAX):
                continue
            A = np.append(A, x)
            if check(A):
                break
        yield A


def random_yes(n_cases):
    for _ in range(n_cases):
        n = np.random.randint(10, 25)
        while True:
            A = np.random.randint(1, MAX + 1, n)
            if check(A):
                break
        yield A


def random_no(n_cases):
    for _ in range(n_cases):
        n = np.random.choice([11, 12, 13, 14])
        while True:
            A = np.random.randint(1, MAX + 1, n)
            if not check(A):
                break
        yield A


def conway_no():
    for N in range(12, 20):
        conway = get_conway(N)
        conway <<= (19 - N)
        assert conway.max() <= MAX

        def get_random_number(e):
            """ 2でちょうど e 回われる"""
            M = MAX >> e
            while True:
                x = np.random.randint(1, M + 1)
                if x & 1:
                    break
            x <<= e
            assert x <= MAX
            return x

        A = np.concatenate([conway, [get_random_number(i) for i in range(19 - N)]]).astype(np.int32)
        np.random.shuffle(A)
        yield A


def conway_yes():
    for N in range(12, 19):
        conway = get_conway(N)
        assert conway.max() <= MAX

        def get_random_number(mod, r):
            r %= mod
            M = (MAX - r) // mod
            return np.random.randint(0, M + 1) * mod + r
        n = 19 - N
        mod = (1 << n) - 1
        conway *= mod
        while True:
            j = np.random.randint(0, mod)
            if np.gcd(mod, j) == 1:
                break
        A = np.concatenate([conway, [get_random_number(mod, j << i) for i in range(n)]]).astype(np.int32)
        np.random.shuffle(A)
        yield A
    for x in [1, MAX - 1]:
        conway = get_conway(19)
        A = np.concatenate([conway, [x, x]])
        yield A
        yield A[::-1]
        np.random.shuffle(A)
        yield A


def large():
    for A in conway_no():
        N = np.random.randint(int(MAX * .9), MAX)
        B = np.random.randint(1, MAX + 1, N)
        B = np.unique(B)
        B = np.setdiff1d(B, A)
        B[: len(A)] = A
        if np.random.randint(0, 2):
            B = B[::-1]
        yield B


def handmade():
    # max
    yield np.random.randint(1, MAX + 1, MAX)
    # 1,2,...,MAX
    yield np.arange(1, MAX + 1)
    # x,x,...,x
    yield np.ones(MAX, np.int32) * np.random.randint(1, MAX + 1)
    # x
    yield np.random.randint(1, MAX + 1, 1)
    # 大きな和になるやつ
    while True:
        A = get_conway(12)
        A *= 127
        A = np.concatenate([A, [149987 - (1 << i) - 127 * np.random.randint(0, 50) for i in range(7)]])
        if check(A):
            break
    yield A
    yield A[::-1]


gens = [small_yes(5), random_yes(5), random_no(5), conway_no(), conway_yes(), large(), handmade()]
write_all(gens)
