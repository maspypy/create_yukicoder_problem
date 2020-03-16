#!/usr/local/bin/python3.8
import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines


def min_pay(a, X, Y, Z):
    x, y, z = 0, 0, 0
    z = min(Z, a // 10000)
    a -= 10000 * z
    y = min(Y, a // 5000)
    a -= 5000 * z
    x = min(X, a // 1000)
    a -= 1000 * x
    if x < X:
        x += 1
    elif y < Y:
        y += 1
    elif z < Z:
        z += 1
    return x, y, z


def solve(A, X, Y, Z):
    """左から順に、その都度の支払い額を最小にしていく"""
    A = (x + 1 for x in A)
    for a in A:
        x, y, z = min_pay(a, X, Y, Z)
        if 1000 * x + 5000 * y + 10000 * z < a:
            return False
        X -= x
        Y -= y
        Z -= z
    return True


N, X, Y, Z, *A = map(int, read().split())
print('Yes' if solve(A, X, Y, Z) else 'No')
