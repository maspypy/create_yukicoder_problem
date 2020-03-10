#!/usr/bin/python3.8
MAX = 10 ** 5


def gen_NO_pattern(maxsize):
    import random
    assert maxsize >= 2
    k = random.choice([0, 1, 2, 3, 4])
    if k == 0:
        n = random.randint(0, maxsize)
        return '-' * n
    if k == 1:
        return '-o-'
    if k == 2:
        n = random.randint(0, maxsize - 1)
        return 'o' + '-' * n
    if k == 3:
        n = random.randint(0, maxsize - 1)
        return '-' * n + 'o'
    if k == 4:
        while True:
            n = random.randint(0, maxsize - 2)
            if n % 2 == 0:
                break
        return 'o' + '-' * n + 'o'


def modify(S):
    o = S.count('o')
    x = S.count('x')
    if o >= x:
        S += 'x' * (o - x)
    elif o < x:
        S += 'xoo' * (x - o)
    return S


def write(ind, S):
    fname = f'03_NO_{ind:02}.in'
    with open(fname, 'w') as f:
        N = len(S)
        f.write(str(N) + '\n')
        f.write(S + '\n')


def gen_NO_board(d):
    while True:
        patterns = []
        L = 0
        while L < 90000:
            p = gen_NO_pattern(maxsize=d)
            if L + len(p) > MAX:
                continue
            patterns.append(p)
            L += len(p) + 1
        S = 'x'.join(patterns)
        S = modify(S)
        if len(S) > MAX:
            continue
        return S


ind = 0
D = [4, 10, 100, 1000, 10000]
for d in D:
    for _ in range(8):
        S = gen_NO_board(d)
        write(ind, S)
        ind += 1
