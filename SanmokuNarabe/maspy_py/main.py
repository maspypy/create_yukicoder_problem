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
            continue
        if o == 2:
            assert T[0] == T[-1] == 'o'
            n = len(T)
            if n % 2 == 1:
                return True
    return False


if __name__ == '__main__':
    T = int(readline())
    for _ in range(T):
        S = readline().rstrip().split()[1]
        print('O' if solve(S) else 'X')
