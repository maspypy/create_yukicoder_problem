#!/usr/bin/python3.8
def gen_cases():
    yield ([1000], 1, 0, 0)
    yield ([1000 * 100], 199, 0, 0)
    yield ([10 ** 9] * (10 ** 5), 10 ** 9, 10 ** 9, 10 ** 9)
    yield ([1001, 1, 1], 2, 1, 0)
    yield ([1999, 5001], 2, 0, 1)


for i, (A, X, Y, Z) in enumerate(gen_cases()):
    fname = f'06_handmade_{i:02}.in'
    N = len(A)
    with open(fname, 'w') as f:
        f.write(f'{N} {X} {Y} {Z}\n')
        A_str = ' '.join(map(str, A))
        f.write(A_str + '\n')
