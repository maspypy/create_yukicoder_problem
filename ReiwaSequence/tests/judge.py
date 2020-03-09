#!/usr/bin/python3.8
import argparse
import numpy as np


class WrongAnswer(Exception):
    pass


parser = argparse.ArgumentParser()
parser.add_argument('--infile')
parser.add_argument('--outfile')
parser.add_argument('--difffile')
args = parser.parse_args()


def is_AC():
    inf = open(args.infile)
    difff = open(args.difffile)
    outf = open(args.difffile)

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
