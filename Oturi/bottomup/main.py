#!/usr/bin/python3.8
import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines


def solve(A, X, Y, Z):
    A = [x + 1 for x in A]
    N = len(A)
    A.sort(key=lambda x: x % 5000)
    for i in range(N):
        x = A[i] % 5000
        use = min((x + 999) // 1000, X)
        A[i] -= use * 1000
        X -= use
        if A[i] < 0:
            A[i] = 0
    Y += X // 5
    A.sort(key=lambda x: x % 10000)
    for i in range(N):
        x = A[i] % 10000
        use = min((x + 4999) // 5000, Y)
        A[i] -= use * 5000
        Y -= use
        if A[i] < 0:
            A[i] = 0
    Z += Y // 2
    use = sum((x + 9999) // 10000 for x in A)
    return use <= Z


if __name__ == '__main__':
    N, X, Y, Z, *A = map(int, read().split())
    print('Yes' if solve(A, X, Y, Z) else 'No')
