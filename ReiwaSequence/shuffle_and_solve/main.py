#!/usr/bin/python3.8
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
    B = A.copy()
    for i in range(N):
        c = ((p >> i) & 1) - ((q >> i) & 1)
        B[i] *= c
    return B


def solve(A):
    N = len(A)
    K = 23
    if N <= K:
        return solve_small(A)
    else:
        A[:K] = solve_small(A[:K])
        A[K:] = 0
        return A


if __name__ == '__main__':
    N = int(readline())
    A = np.array(read().split(), np.int32)
    ind = np.arange(N)
    np.random.shuffle(ind)
    inv = np.argsort(ind)

    Ashuffle = A[ind]
    B = solve(Ashuffle)
    if B is None:
        print('No')
    else:
        B = B[inv]
        print('Yes')
        print(' '.join(B.astype(str)))
