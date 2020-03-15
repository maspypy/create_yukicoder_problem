#!/usr/bin/python3.8
import sys
import pathlib
me = pathlib.Path(__file__)
prob_dir = str(me.parent.parent)
sys.path.append(prob_dir)
from maspy_py.main import solve
import random
from functools import partial


MAX_S = 1000
MAX_T = 100


def write_case(category_name, id, g):
    fname = category_name + '_' + f'{id:02}' + '.in'
    dataset = list(g)
    with open(fname, 'w') as f:
        T = len(dataset)
        f.write(f'{T}\n')
        for S in dataset:
            N = len(S)
            f.write(f'{N} {S}\n')


def small_yes():
    n = random.randint(5, 15)
    while True:
        S = ''.join(random.choice('ox-') for _ in range(n))
        if S.count('o') != S.count('x'):
            continue
        if solve(S):
            return S


def small_no():
    n = random.randint(1, 15)
    while True:
        S = ''.join(random.choice('ox-') for _ in range(n))
        if S.count('o') != S.count('x'):
            continue
        if not solve(S):
            return S


def modify(S):
    o = S.count('o')
    x = S.count('x')
    if o >= x:
        S += 'x' * (o - x)
    elif o < x:
        S += 'xoo' * (x - o)
    return S


def large_no_board(param):
    """param: 1/deisity.
    if param is large: very sparse board is generated.
    we assume that 2 <= param < MAX_S"""
    def gen_NO_pattern(maxsize):
        import random
        assert maxsize >= 2
        k = random.choice([0, 1, 2, 3, 4])
        if k == 0:
            n = random.randint(0, maxsize)
            return '-' * n
        if k == 1:
            return '-o-'
        if k == 2:
            n = random.randint(0, maxsize - 1)
            return 'o' + '-' * n
        if k == 3:
            n = random.randint(0, maxsize - 1)
            return '-' * n + 'o'
        if k == 4:
            while True:
                n = random.randint(0, maxsize - 2)
                if n % 2 == 0:
                    break
            return 'o' + '-' * n + 'o'
    while True:
        patterns = []
        L = 0
        while L < 900:
            p = gen_NO_pattern(param)
            if L + len(p) > MAX_S:
                continue
            patterns.append(p)
            L += len(p) + 1
        S = 'x'.join(patterns)
        S = modify(S)
        if len(S) > MAX_S:
            continue
        return S


def large_yes_board(param):
    """param: 1/deisity.
    if param is large: very sparse board is generated.
    we assume that 2 <= param < MAX_S"""
    def gen_YES_1():
        while True:
            S = large_no_board(param)
            L = random.randint(0, len(S) - 3)
            R = L + 3
            S = list(S)
            S[L:R] = ['o', 'o', 'o']
            S = ''.join(S)
            S = modify(S)
            if len(S) <= MAX_S:
                return S

    def gen_YES_2():
        while True:
            S = large_no_board(param)
            L = random.randint(0, len(S) - 3)
            R = L + 3
            S = list(S)
            S[L:R] = ['o', 'o', '-']
            S = ''.join(S)
            S = modify(S)
            if len(S) <= MAX_S:
                return S

    def gen_YES_3():
        while True:
            S = large_no_board(param)
            L = random.randint(0, len(S) - 3)
            R = L + 3
            S = list(S)
            S[L:R] = ['o', 'o', '-']
            S = ''.join(S)
            S = modify(S)
            if len(S) <= MAX_S:
                return S

    def gen_YES_4():
        while True:
            S = large_no_board(param)
            while True:
                L = random.randint(0, len(S) - 1)
                R = random.randint(0, len(S) - 1)
                if L + 4 < R and (R - L) % 2 == 0:
                    break
            S = list(S)
            S[L] = 'x'
            S[L + 1] = 'o'
            S[R - 1] = 'o'
            S[R] = 'x'
            S[L + 2:R - 1] = ['-'] * (R - L - 3)
            S = ''.join(S)
            S = modify(S)
            if len(S) <= MAX_S:
                return S

    funcs = [gen_YES_1, gen_YES_2, gen_YES_3, gen_YES_4]
    f = random.choice(funcs)
    return f()


def handmade():
    n = random.randint(0, 2)
    if n == 0:
        return '-' * MAX_S
    if n == 1:
        return 'ox' * (MAX_S // 2)
    if n == 2:
        return 'o' * (MAX_S // 2) + 'x' * (MAX_S // 2)


def gen_dataset(funcs, T):
    for _ in range(T):
        f = random.choice(funcs)
        yield f()


gens = []
funs = [small_yes, small_no]
gens.append(gen_dataset(funs, 10))
gens.append(gen_dataset(funs, 10))
gens.append(gen_dataset(funs, 100))
gens.append(gen_dataset(funs, 100))
gens.append(gen_dataset(funs, 100))
gens.append(gen_dataset(funs, 100))
funs = [small_yes, small_no, partial(large_no_board, 10), partial(large_no_board, 100),
        partial(large_yes_board, 10), partial(large_yes_board, 100), handmade]
gens.append(gen_dataset(funs, 100))
gens.append(gen_dataset(funs, 100))
funs = [partial(large_no_board, 10), partial(large_no_board, 100),
        partial(large_yes_board, 10), partial(large_yes_board, 100), handmade]
gens.append(gen_dataset(funs, 100))
gens.append(gen_dataset(funs, 100))


def write_all(gens):
    for i, g in enumerate(gens):
        category_name = f'02_dataset'
        write_case(category_name, i, g)


write_all(gens)
