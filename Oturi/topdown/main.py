#!/usr/local/bin/python3.8
import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines


def solve(A, X, Y, Z):
    A = [x + 1 for x in A]
    N = len(A)
    for (cost, num) in [(10000, Z), (5000, Y), (1000, X)]:
        A.sort(reverse=True)
        for i in range(N):
            x = A[i] // cost
            use = min(x, num)
            A[i] -= use * cost
            num -= use
        A.sort(reverse=True)
        for i in range(min(N, num)):
            A[i] = 0
    return sum(A) == 0


if __name__ == '__main__':
    N, X, Y, Z, *A = map(int, read().split())
    print('Yes' if solve(A, X, Y, Z) else 'No')
