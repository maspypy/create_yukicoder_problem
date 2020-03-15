#!/usr/local/bin/python3.8
import numpy as np
import sys


def rime_judge_streams():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--infile')
    parser.add_argument('--outfile')
    parser.add_argument('--difffile')
    args = parser.parse_args()
    inf = open(args.infile)
    difff = open(args.difffile)
    outf = open(args.outfile)
    return inf, difff, outf


def yuki_judge_streams():
    args = sys.argv
    inf = open(args[1])
    difff = open(args[2])
    outf = sys.stdin
    return inf, difff, outf


inf, difff, outf = rime_judge_streams()
# inf, difff, outf = yuki_judge_streams()


class WrongAnswer(Exception):
    pass


def is_AC():
    _ = int(inf.readline())
    A = np.array(inf.readline().split(), np.int32)

    diff_ans = difff.readline().rstrip()
    if diff_ans == 'No':
        return outf.read() == 'No\n'
    elif diff_ans == 'Yes':
        out_ans = outf.readline().rstrip()
        if out_ans != 'Yes':
            return False
        B = np.array(outf.readline().split(), np.int32)
        if B.sum() != 0:
            return False
        if np.all(B == 0):
            return False
        return np.all((B == A) | (B == 0) | (B == -A))


if not is_AC():
    raise WrongAnswer
