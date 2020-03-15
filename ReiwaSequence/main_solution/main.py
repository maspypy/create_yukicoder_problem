#!/usr/local/bin/python3.8
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
import numpy as np


def solve_small(A):
    N = len(A)
    dp = np.zeros(1 << N, np.int32)
    for i, x in enumerate(A):
        dp[1 << i:1 << (i + 1)] = dp[:1 << i] + x
    counts = np.bincount(dp)
    if np.all(counts < 2):
        return None
    S = np.where(counts >= 2)[0][0]
    ind = np.where(dp == S)[0]
    p = ind[0]
    q = ind[1]
    for i in range(N):
        c = ((p >> i) & 1) - ((q >> i) & 1)
        A[i] *= c
    return A


def solve(A):
    N = len(A)
    K = 22
    if N <= K:
        return solve_small(A.copy())
    else:
        B = A.copy()
        B[:K] = solve_small(A[:K].copy())
        B[K:] = 0
        return B


if __name__ == '__main__':
    N = int(readline())
    A = np.array(read().split(), np.int32)
    B = solve(A)
    if B is None:
        print('No')
    else:
        print('Yes')
        print(' '.join(B.astype(str)))
