#!/usr/bin/python3.8
import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

import numpy as np

S = readline().rstrip()
N, K = map(int, read().split())


def suffix_array(S):
    N = len(S)

    n = 1
    key = np.array([ord(x) for x in S])
    for _ in range(N.bit_length() + 1):
        ind = key.argsort()
        key_sort = key[ind]
        # 同じ数はまとめる
        cls = np.ones(N, np.int64)
        cls[1:] = (key_sort[1:] != key_sort[:-1])
        np.cumsum(cls, out=cls)
        rank = np.empty_like(cls)
        rank[ind] = cls
        if n >= N:
            break
        n *= 2
        key = rank * (cls[-1] + 10)
        key[:-n // 2] += rank[n // 2:]
    return ind, rank - 1


if N == 1:
    SA, ISA = suffix_array(S)
    print(1 + SA[K - 1])
    exit()

SA, ISA = suffix_array(S * 2)
# 長さを並べる
SA = len(S) * 2 - SA
LS = len(S)
rest = K
answer = 0
for x in SA.tolist():
    if x <= LS:
        if rest == 1:
            answer = x
            break
        else:
            rest -= 1
            continue
    if rest <= N - 1:
        answer = x + (rest - 1) * LS
        break
    else:
        rest -= (N - 1)
        continue

print(answer)
