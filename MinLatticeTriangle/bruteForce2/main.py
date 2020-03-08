#!/usr/bin/python3.8
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
from numba import njit
from math import gcd

MOD = 10**9 + 7


@njit
def solve(N):
    ret = 0
    M = 1
    while (M + 1) ** 2 <= N:
        M += 1
    for x in range(-M, M + 1):
        for y in range(-M, M + 1):
            if x * x + y * y <= N:
                if gcd(x, y) == 1:
                    ret += abs(x) + abs(y)
                    ret %= MOD
    return (6 * ret - 16) % MOD


N = int(read())
print(solve(N))
