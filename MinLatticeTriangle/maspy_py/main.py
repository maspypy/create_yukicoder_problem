#!/usr/local/bin/python3.8
import sys
read = sys.stdin.buffer.read1
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
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
    mu = np.ones(N, np.int8)
    mu[0] = 0
    for p in primes:
        mu[p::p] *= - 1
    for p in primes:
        pp = p * p
        if pp >= N:
            break
        mu[pp::pp] = 0
    return mu


def F(N):
    """return sum(|x| + |y|) for lattice points (x,y), satisfying x^2 + y^2 <= N"""
    x_max = int(N ** .5)
    x = np.arange(1, x_max + 1, dtype=np.int64)
    y_max = np.sqrt(N - x * x).astype(int)
    S_xplus = (x * (1 + 2 * y_max)).sum() % MOD
    return S_xplus


def f(N):
    Nsq = int(N ** .5)
    is_prime, primes = prime_table(Nsq + 10)
    mu = mobius_table(Nsq + 10, primes)
    mu_d = mu * np.arange(Nsq + 10)
    mu_d_cum = mu_d.cumsum() % MOD
    M = int(N ** (1 / 3))
    x = 0
    for d in range(1, N + 1):
        n = N // (d * d)
        if n <= M:
            break
        x += mu_d[d] * F(n)
    x %= MOD
    for n in range(1, M + 1):
        dr = int((N // n) ** .5)
        dl = int((N // (n + 1)) ** .5)
        x += (mu_d_cum[dr] - mu_d_cum[dl]) * F(n) % MOD
    return (24 * x - 16) % MOD


print(f(N))
