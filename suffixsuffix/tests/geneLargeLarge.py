#!/usr/bin/python3.8
import random

alphabets = [chr(ord('a') + x) for x in range(26)]


def gen_random_word(N, M):
    random.shuffle(alphabets)
    return ''.join(random.choice(alphabets[:M]) for _ in range(N))


def gen_test_cases():
    for M in [1, 2, 3, 3, 26, 26]:
        size = random.randint(90000, 100000)
        rep = random.randint(10**7, 10**9)
        S = gen_random_word(size, M)
        K = random.randint(1, len(S) * rep)
        yield (S, rep, K)


for ind, (S, N, K) in enumerate(gen_test_cases()):
    fname = f'05_large_large_{ind:02}.in'
    with open(fname, 'w') as f:
        f.write(S + '\n')
        f.write(str(N) + ' ' + str(K) + '\n')
