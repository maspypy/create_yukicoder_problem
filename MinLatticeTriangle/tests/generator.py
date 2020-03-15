#!/usr/local/bin/python3.8
import random


def write_case(category_name, id, N):
    fname = category_name + '_' + f'{id:02}' + '.in'
    with open(fname, 'w') as f:
        f.write(str(N) + '\n')


def write_all(gens):
    for i, g in enumerate(gens, 2):
        category_name = f'{i:02}_{g.__name__}'  # 02_small など
        for j, N in enumerate(g):
            write_case(category_name, j, N)


def small(n_cases):
    for _ in range(n_cases):
        yield random.randint(10, 100)


def middle(n_cases):
    for _ in range(n_cases):
        yield random.randint(10**5, 10**6)


def large(n_cases):
    for _ in range(n_cases):
        yield random.randint(5 * 10**11, 10**12)


def hand():
    # max
    yield 10 ** 12
    # square - 1
    yield 10 ** 12 - 1
    # prime^2
    yield 999983**2
    yield 999961 ** 2


gens = [small(5), middle(5), large(10), hand()]
write_all(gens)
