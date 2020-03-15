#!/usr/local/bin/python3.8
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


def prime_table(N):
    is_prime = np.zeros(N + 1, np.bool)
    is_prime[2] = 1
    is_prime[3::2] = 1
    for p in range(3, N, 2):
        if p * p >= N:
            break
        if is_prime[p]:
            is_prime[p * p:: p + p] = 0
    primes = np.where(is_prime)[0]
    return is_prime, primes


is_prime, primes = prime_table(10 ** 5 + 10)


# repeated 対策
def to_standard_form(S, N):
    for p in primes:
        if p > len(S):
            break
        while True:
            L = len(S)
            if L % p != 0:
                break
            dx = L // p
            repeated = True
            for i in range(1, p):
                if S[i * dx: i * dx + dx] != S[:dx]:
                    repeated = False
                    break
            if not repeated:
                break
            S = S[:dx]
            N *= p
    return S, N


S, N = to_standard_form(S, N)

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

# 長さを持ったので、インデックスに戻す
answer = LS * N + 1 - answer
print(answer)
