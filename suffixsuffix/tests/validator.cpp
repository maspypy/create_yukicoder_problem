#include "testlib.h"
#include <bits/stdc++.h>
using namespace std;
using Int = long long;
const Int MIN_N = 1;
const Int MAX_N = 1e5;
const Int MIN_M = 1;
const Int MAX_M = 1e9;
const Int MIN_Q = 1;
const Int MAX_Q = 1e5;
const Int MIN_K = 1;

signed main(int argc, char *argv[])
{
    registerValidation(argc, argv);
    Int N = inf.readLong(MIN_N, MAX_N, "N");
    inf.readSpace();
    Int M = inf.readLong(MIN_M, MAX_M, "M");
    inf.readSpace();
    Int Q = inf.readLong(MIN_Q, min(MAX_Q, N * M), "Q");
    inf.readEoln();
    string S = inf.readToken("[a-z]+");
    ensuref(S.size() == N, "|S| == N does not hold.");
    inf.readEoln();
    Int prev = 0;
    Int MAX_K = N * M;
    for (int i = 0; i < Q; i++)
    {
        if (i)
            inf.readSpace();
        Int K = inf.readLong(MIN_K, MAX_K, "K");
        ensuref(prev <= K, "K_i must be increasing.");
        prev = K;
    }
    inf.readEoln();
    inf.readEof();
    return 0;
}
