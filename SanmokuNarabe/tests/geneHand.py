#!/usr/bin/python3.8


def write(ind, S):
    fname = f'05_handmade_{ind:02}.in'
    with open(fname, 'w') as f:
        N = len(S)
        f.write(str(N) + '\n')
        f.write(S + '\n')


def gen_cases():
    # 長さ 1
    yield '-'
    # 最小
    yield 'xo'
    # 最大
    N = 10 ** 5
    yield '-' * N
    yield 'xo' + '-' * (N - 4) + 'ox'
    yield 'o' + '-' * (N - 4) + 'oxx'
    yield 'xo' + '-' * (N - 5) + 'ox'
    yield 'ox' * (N // 2)


ind = 0
for S in gen_cases():
    write(ind, S)
    ind += 1
