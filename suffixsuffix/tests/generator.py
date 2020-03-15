#!/usr/local/bin/python3.8
import random
import numpy as np
MAX_K = 10 ** 5

alphabets = [chr(ord('a') + x) for x in range(26)]


def make_K(N, M):
    if N * M <= MAX_K:
        return np.arange(1, N * M + 1)
    K = np.random.randint(1, N * M + 1, MAX_K * 3)
    Q = np.random.randint(int(0.9 * MAX_K), MAX_K + 1)
    return np.unique(K)[:Q]


def write_case(category_name, id, S, M):
    fname = category_name + '_' + f'{id:02}' + '.in'
    N = len(S)
    K = make_K(N, M)
    Q = len(K)
    K_str = ' '.join(K.astype(str))
    with open(fname, 'w') as f:
        f.write(f'{N} {M} {Q}\n')
        f.write(S + '\n')
        f.write(K_str + '\n')


def write_all(gens):
    for i, g in enumerate(gens, 2):
        category_name = f'{i:02}_{g.__name__}'  # 02_small など
        for j, (S, M) in enumerate(g):
            write_case(category_name, j, S, M)


def make_random_word(N, x):
    """make a string of length N consist of x alphabets"""
    random.shuffle(alphabets)
    return ''.join(random.choice(alphabets[:x]) for _ in range(N))


def small_small(n_alphabets):
    """n_alphabets: list of integers"""
    for n in n_alphabets:
        N = random.randint(5, 10)
        M = random.randint(2, 5)
        S = make_random_word(N, n)
        yield (S, M)


gens = [small_small([2, 3, 4, 26, 26])]
write_all(gens)
