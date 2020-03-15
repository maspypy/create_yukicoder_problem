#!/usr/local/bin/python3.8
import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

S = readline().rstrip()
N, K = map(int, read().split())

S *= N
SA = sorted(range(1, len(S) + 1), key=lambda i: S[i - 1:])
print(SA[K - 1])
