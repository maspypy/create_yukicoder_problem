#!/usr/local/bin/python3.8
import itertools
import sys
read = sys.stdin.buffer.read1


def gen_points(N):
    M = 1
    while (M + 1) ** 2 <= N:
        M += 1
    for x, y in itertools.product(range(-M, M + 1), repeat=2):
        if x * x + y * y <= N:
            yield (x, y)


def solve(N):
    ret = 0
    for x1, y1 in gen_points(N):
        for x2, y2 in gen_points(N):
            if abs(x1 * y2 - x2 * y1) == 1:
                ret += abs(x1) + abs(x2) + abs(y1) + abs(y2)
    return ret // 2


N = int(read())
print(solve(N))
