#!/usr/bin/python3.8
import random

alphabets = [chr(ord('a') + x) for x in range(26)]


def gen_random_word(N, M):
    random.shuffle(alphabets)
    return ''.join(random.choice(alphabets[:M]) for _ in range(N))


def gen_test_cases():
    for rep in [10**2, 10**4, 10**9]:
        for M in range(1, 11, 2):
            S = gen_random_word(10, M)
            K = random.randint(1, len(S) * rep)
            yield (S, rep, K)


for ind, (S, N, K) in enumerate(gen_test_cases()):
    fname = f'04_small_large_{ind:02}.in'
    with open(fname, 'w') as f:
        f.write(S + '\n')
        f.write(str(N) + ' ' + str(K) + '\n')
