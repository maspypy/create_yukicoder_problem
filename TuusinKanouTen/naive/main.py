#!/usr/bin/env python3
# %%
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
from numba import njit
from math import gcd

# %%
N, MOD = map(int, read().split())

# %%
@njit
def f(N, x, MOD):
    ret = 0
    for y in range(N + 10):
        if x * x + y * y > N * N:
            break
        if gcd(abs(x), abs(y)) != 1:
            continue
        if y == 0:
            ret += x
        else:
            ret += 2 * x
    return 4 * ret % MOD

def solve(N, MOD):
    ret = 0
    for x in range(N + 10):
        if x % 1000 == 0:
            print(x)
        ret += f(N, x, MOD)
    return ret % MOD


# %%
MOD = 10**9 + 7
solve(5, 10 ** 9 + 7), solve(12345, MOD)

# %%
solve(10**6, MOD)
# %%
print(solve(N, MOD))
