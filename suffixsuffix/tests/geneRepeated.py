#!/usr/bin/python3.8
import random

alphabets = [chr(ord('a') + x) for x in range(26)]


def gen_random_word(N, M):
    random.shuffle(alphabets)
    return ''.join(random.choice(alphabets[:M]) for _ in range(N))


def gen_test_cases():
    for _ in range(20):
        rep = random.randint(2, 10**4)
        size = (10**5) // rep
        M = random.randint(2, 26)
        S = gen_random_word(size, M) * rep
        N = random.randint(10**8, 10**9)
        K = random.randint(1, len(S) * rep)
        yield (S, N, K)


for ind, (S, N, K) in enumerate(gen_test_cases()):
    fname = f'06_repeated_{ind:02}.in'
    with open(fname, 'w') as f:
        f.write(S + '\n')
        f.write(str(N) + ' ' + str(K) + '\n')
