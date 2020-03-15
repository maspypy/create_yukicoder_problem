#!/usr/local/bin/python3.8
import random
import numpy as np
MAX_Q = 10 ** 5
MAX_N = 10 ** 5
MAX_M = 10 ** 9

alphabets = [chr(ord('a') + x) for x in range(26)]


def make_K(N, M):
    if N * M <= MAX_Q:
        return np.arange(1, N * M + 1)
    K = np.random.randint(1, N * M + 1, MAX_Q * 3)
    Q = np.random.randint(int(0.9 * MAX_Q), MAX_Q + 1)
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
    for n in n_alphabets:
        N = random.randint(5, 10)
        M = random.randint(2, 5)
        S = make_random_word(N, n)
        yield (S, M)


def M_equal_1(n_alphabets):
    for n in n_alphabets:
        N = random.randint(int(MAX_N * .9), MAX_N)
        M = 1
        S = make_random_word(N, n)
        yield (S, M)


def large_small(n_alphabets):
    for n in n_alphabets:
        N = random.randint(int(MAX_N * .9), MAX_N)
        M = random.randint(10**5, MAX_M)
        S = make_random_word(N, n)
        yield (S, M)


def small_large(n_alphabets):
    for n in n_alphabets:
        N = random.randint(5, 10)
        M = random.randint(10**5, MAX_M)
        S = make_random_word(N, n)
        yield (S, M)


def large_large(n_alphabets):
    for n in n_alphabets:
        N = random.randint(int(MAX_N * .9), MAX_N)
        M = random.randint(10**5, MAX_M)
        S = make_random_word(N, n)
        yield (S, M)


def repeated(n_alphabets):
    for n in n_alphabets:
        rep = random.randint(2, 10**4)
        size = (10**5) // rep
        S = make_random_word(size, n) * rep
        M = random.randint(10**5, MAX_M)
        yield (S, M)


def handmade():
    # smallest
    yield 'a', 1
    yield 'a', MAX_M
    # monotone max
    yield 'a' * MAX_N, MAX_M
    # random max
    yield make_random_word(MAX_N, 26), MAX_M


n_alphabets = [2, 3, 4, 26, 26]
gens = [small_small(n_alphabets), M_equal_1(n_alphabets), large_small(n_alphabets),
        small_large(n_alphabets), large_large(n_alphabets), repeated(n_alphabets), handmade()]
write_all(gens)
