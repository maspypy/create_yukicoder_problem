#!/usr/bin/python3.8
import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines


def solve(S):
    win_words = ['ooo', '-oo', 'oo-', 'o-o', '-o--', '--o-']
    for word in win_words:
        if S.find(word) != -1:
            return True
    S = 'x' + S + 'x'
    for T in S.split('x'):
        o = T.count('o')
        assert o <= 2
        if o <= 1:
            return False
        if o == 2:
            assert T[0] == T[-1] == 'o'
            n = len(T)
            return n % 2 == 1


if __name__ == '__main__':
    N = int(readline())
    S = read().rstrip()
    print('O' if solve(S) else 'X')
