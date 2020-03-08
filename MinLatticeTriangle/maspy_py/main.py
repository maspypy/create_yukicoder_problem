#!/usr/bin/python3.8
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
from functools import lru_cache
import numpy as np
MOD = 10 ** 9 + 7

N = int(read())


def prime_table(N):
    is_prime = np.zeros(N, np.bool)
    is_prime[2] = 1
    is_prime[3::2] = 1
    for p in range(3, N, 2):
        if p * p >= N:
            break
        if is_prime[p]:
            is_prime[p * p:: p + p] = 0
    primes = np.where(is_prime)[0]
    return is_prime, primes


def mobius_table(N, primes):
    mu = np.ones(N, np.int64)
    mu[0] = 0
    for p in primes:
        mu[p::p] *= -1
        pp = p * p
        if p < N:
            mu[pp::pp] = 0
    return mu


@lru_cache(None)
def F(N):
    """return sum(|x| + |y|) for lattice points (x,y), satisfying x^2 + y^2 <= N"""
    x_max = int(N ** .5)
    x = np.arange(1, x_max + 1, dtype=np.int64)
    y_max = np.sqrt(N - x * x).astype(int)
    S_xplus = (x * (1 + 2 * y_max) % MOD).sum() % MOD
    return S_xplus % MOD


def f(N):
    Nsq = int(N ** .5)
    is_prime, primes = prime_table(Nsq + 10)
    mu = mobius_table(Nsq + 10, primes)
    F_values = np.array([0] + [F(N // (n * n)) for n in range(1, Nsq + 1)], np.int64)
    x = (mu[: Nsq + 1] * F_values * np.arange(Nsq + 1, dtype=np.int64) % MOD).sum() % MOD
    return 48 * x - 16


print(f(N))
