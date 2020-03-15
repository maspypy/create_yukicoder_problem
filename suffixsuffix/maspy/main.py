#!/usr/local/bin/python3.8
import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
import numpy as np

N, M, Q = map(int, readline().split())
S = readline().rstrip()
K = tuple(map(int, read().split()))


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
def to_standard_form(S, M):
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
            M *= p
    return S, M


S, M = to_standard_form(S, M)
if M == 1:
    SA, ISA = suffix_array(S)
    K = np.array(K)
    answers = 1 + SA[K - 1]
    print(' '.join(answers.astype(str)))
    exit()


SA, ISA = suffix_array(S * 2)
# 長さを並べる
N = len(S)
SA = (N * 2 - SA)
answer = [0] * Q
i = 0
ind = 1
for x in SA.tolist():
    if x <= N:
        n = 1
    else:
        n = M - 1
    while i < Q and K[i] < ind + n:
        answer[i] = N * (M - K[i] + ind) + 1 - x
        i += 1
    ind += n

# 長さを持ったので、インデックスに戻す
print(' '.join(map(str, answer)))
