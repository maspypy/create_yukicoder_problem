#!/usr/bin/python3.8
from geneNo import gen_NO_board, modify
import random

MAX = 10 ** 5


def write(ind, S):
    fname = f'04_YES_{ind:02}.in'
    with open(fname, 'w') as f:
        N = len(S)
        f.write(str(N) + '\n')
        f.write(S + '\n')


def gen_YES_1():
    while True:
        S = gen_NO_board(10)
        L = random.randint(0, len(S) - 3)
        R = L + 3
        S = list(S)
        S[L:R] = ['o', 'o', 'o']
        S = ''.join(S)
        S = modify(S)
        if len(S) <= MAX:
            yield S


def gen_YES_2():
    while True:
        S = gen_NO_board(10)
        L = random.randint(0, len(S) - 3)
        R = L + 3
        S = list(S)
        S[L:R] = ['o', 'o', '-']
        S = ''.join(S)
        S = modify(S)
        if len(S) <= MAX:
            yield S


def gen_YES_3():
    while True:
        S = gen_NO_board(10)
        L = random.randint(0, len(S) - 4)
        R = L + 4
        S = list(S)
        S[L:R] = ['-', 'o', '-', '-']
        S = ''.join(S)
        S = modify(S)
        if len(S) <= MAX:
            yield S


def gen_YES_4():
    while True:
        S = gen_NO_board(10)
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
        if len(S) <= MAX:
            yield S


ind = 0
gens = [gen_YES_1(), gen_YES_2(), gen_YES_3(), gen_YES_4()]
for f in gens:
    for _ in range(10):
        S = next(f)
        write(ind, S)
        ind += 1
