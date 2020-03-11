#!/usr/bin/python3.8
import sys
import pathlib
import random
me = pathlib.Path(__file__)
prob_dir = str(me.parent.parent)
sys.path.append(prob_dir)
from topdown.main import solve


MAX = 10**9


def gen_NO():
    while True:
        while True:
            N = random.randint(9 * 10 ** 4, 10 ** 5)
            A = [random.randint(1, 10 ** random.randint(3, 9)) for _ in range(N)]
            if not solve(A, MAX, MAX, MAX):
                continue
            break
        dx = 1 << 29
        nums = [0, 0, 0]
        while True:
            ind = [0, 1, 2]
            random.shuffle(ind)
            for i in ind:
                nums[i] += dx
                if solve(A, *nums):
                    nums[i] -= dx
                    continue
            dx //= 2
            if not dx:
                break
        if max(nums) > 10 ** 9:
            continue
        return A, *nums


def gen_YES():
    A, X, Y, Z = gen_NO()
    X += 1
    return A, X, Y, Z


for i in range(5):
    fname = f'04_large_YES_{i:02}.in'
    A, X, Y, Z = gen_YES()
    N = len(A)
    with open(fname, 'w') as f:
        f.write(f'{N} {X} {Y} {Z}\n')
        A_str = ' '.join(map(str, A))
        f.write(A_str + '\n')


for i in range(5):
    fname = f'05_large_NO_{i:02}.in'
    A, X, Y, Z = gen_NO()
    N = len(A)
    with open(fname, 'w') as f:
        f.write(f'{N} {X} {Y} {Z}\n')
        A_str = ' '.join(map(str, A))
        f.write(A_str + '\n')
