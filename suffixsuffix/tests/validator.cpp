#include "testlib.h"
#include <bits/stdc++.h>
using namespace std;
using Int = long long;
const int MIN_LS = 1;
const int MAX_LS = 1e5;
const Int MIN_N = 1;
const Int MAX_N = 1e9;

signed main(int argc, char *argv[])
{
    registerValidation(argc, argv);
    string S = inf.readToken("[a-z]+");
    ensuref(MIN_LS <= S.size() && S.size() <= MAX_LS, "The size of S is invalid.");
    inf.readEoln();
    Int N = inf.readLong(MIN_N, MAX_N, "N");
    inf.readSpace();
    Int MIN_K = 1;
    Int MAX_K = N * S.size();
    inf.readLong(MIN_K, MAX_K, "K");
    inf.readEoln();
    inf.readEof();
    return 0;
}
