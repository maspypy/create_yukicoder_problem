#!/usr/local/bin/python3.8
import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

import numpy as np

N, M, Q = map(int, readline().split())
S = readline().rstrip()
K = list(map(int, read().split()))


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


S *= M
SA, ISA = suffix_array(S)
answers = (1 + SA[i - 1] for i in K)
print(' '.join(map(str, answers)))
