#!/usr/local/bin/python3.8
import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

N, M, Q = map(int, readline().split())
S = readline().rstrip()
K = list(map(int, read().split()))

S *= M
SA = sorted(range(1, len(S) + 1), key=lambda i: S[i - 1:])
answers = (SA[i - 1] for i in K)
print(' '.join(map(str, answers)))
