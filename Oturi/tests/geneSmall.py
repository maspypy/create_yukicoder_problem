#!/usr/local/bin/python3.8
import sys
import pathlib
import random
me = pathlib.Path(__file__)
prob_dir = str(me.parent.parent)
sys.path.append(prob_dir)
from topdown.main import solve


def gen_YES():
    N = random.randint(1, 10)
    A = [random.randint(1, 30000) for _ in range(N)]
    X, Y, Z = 0, 0, 0
    while True:
        if solve(A, X, Y, Z):
            break
        r = random.randint(0, 2)
        if r == 0:
            X += 1
        elif r == 1:
            Y += 1
        else:
            Z += 1
    while True:
        if X and solve(A, X - 1, Y, Z):
            X -= 1
        elif Y and solve(A, X, Y - 1, Z):
            Y -= 1
        elif Z and solve(A, X, Y, Z - 1):
            Z -= 1
        else:
            return A, X, Y, Z


def gen_NO():
    while True:
        A, X, Y, Z = gen_YES()
        if X == Y == Z == 0:
            continue
        break
    while True:
        r = random.randint(0, 2)
        if r == 0 and X > 0:
            return A, X - 1, Y, Z
        if r == 1 and Y > 0:
            return A, X, Y - 1, Z
        if r == 2 and Z > 0:
            return A, X, Y, Z - 1


for i in range(20):
    fname = f'02_small_YES_{i:02}.in'
    A, X, Y, Z = gen_YES()
    N = len(A)
    with open(fname, 'w') as f:
        f.write(f'{N} {X} {Y} {Z}\n')
        A_str = ' '.join(map(str, A))
        f.write(A_str + '\n')


for i in range(20):
    fname = f'03_small_NO_{i:02}.in'
    A, X, Y, Z = gen_NO()
    N = len(A)
    with open(fname, 'w') as f:
        f.write(f'{N} {X} {Y} {Z}\n')
        A_str = ' '.join(map(str, A))
        f.write(A_str + '\n')
