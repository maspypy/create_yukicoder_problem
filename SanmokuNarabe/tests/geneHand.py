#!/usr/bin/python3.8


def write(ind, A):
    n = len(A)
    fname = f'05_handmade_{ind:02}.in'
    with open(fname, 'w') as f:
        f.write(f'{n}\n')
        A_str = ' '.join(map(str, A))
        f.write(f'{A_str}\n')
    return


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
    yield 'xo' + '-' * (N - 3) + 'ox'
    yield 'ox' * (N // 2)


ind = 0
for S in gen_cases():
    write(ind, S)
    ind += 1
