#!/usr/local/bin/python3.8
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
import numpy as np


def solve(A):
    return np.zeros_like(A)


if __name__ == '__main__':
    N = int(readline())
    A = np.array(read().split(), np.int32)
    B = solve(A)
    if B is None:
        print('No')
    else:
        print('Yes')
        print(' '.join(B.astype(str)))
