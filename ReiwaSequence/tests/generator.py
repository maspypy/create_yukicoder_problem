#!/usr/bin/python3.8
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
        n = np.random.randint(10, 30)
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


def powerof2_no():
    K = 18
    A = np.empty(K, np.int32)
    for i in range(K):
        x = 1 << i
        n = np.random.randint(0, (MAX - x) // (x + x) + 1)
        A[i] = x * (n + n + 1)
    np.random.shuffle(A)
    return A


def conway_no():
    conway = np.array([
        66844, 100551, 117547, 126045, 130368,
        132568, 133688, 134258, 134543, 134691,
        134768, 134808, 134828, 134839, 134845,
        134848, 134850, 134851, 134852], np.int32)
    while True:
        n = np.random.randint(0, MAX - conway[-1] + 1)
        A = conway + n
        if not check(A):
            np.random.shuffle(A)
            return A


def worst_no(n_size):
    funs = [conway_no, powerof2_no]
    for i in range(n_size):
        f = funs[i & 1]
        yield f()


def worst_yes(n_size):
    for A in worst_no(n_size):
        x = np.random.randint(1, MAX + 1)
        A = np.append(A, x)
        if np.random.randint(0, 2):
            A = A[::-1]
        yield A


def large(n_size):
    for A in worst_no(n_size):
        N = np.random.randint(int(MAX * .9), MAX)
        B = np.random.randint(1, MAX + 1, N)
        B = np.unique(B)
        B = np.setdiff1d(B, A)
        B[: len(A)] = A
        if np.random.randint(0, 2):
            B = B[::-1]
        yield B


def unique_yes(n_size):
    for _ in range(n_size):
        A = [1]
        while True:
            x = sum(A) + np.random.randint(1, 4)
            if x > MAX:
                break
            A.append(x)
        A.pop()
        A.append(sum(A))
        A = np.array(A)
        np.random.shuffle(A)
        yield A


def handmade():
    # max
    yield np.random.randint(1, MAX + 1, MAX)
    # 1,2,...,MAX
    yield np.arange(1, MAX + 1)
    # x,x,...,x
    yield np.ones(MAX, np.int32) * np.random.randint(1, MAX + 1)


gens = [small_yes(5), random_yes(5), random_no(5), worst_no(10), large(10), unique_yes(10), handmade()]
write_all(gens)
