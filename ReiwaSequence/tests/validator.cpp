#include "testlib.h"
#include <bits/stdc++.h>
using namespace std;
using Int = long long;
const Int MIN_N = 1;
const Int MAX_N = 300000;
const Int MIN_A = 1;
const Int MAX_A = 300000;

signed main(int argc, char *argv[])
{
    registerValidation(argc, argv);
    int N = inf.readInt(MIN_N, MAX_N, "N");
    inf.readEoln();
    for (int i = 0; i < N; i++)
    {
        if (i)
        {
            inf.readSpace();
        }
        int a = inf.readInt(MIN_A, MAX_A, "A");
    }
    inf.readEoln();
    inf.readEof();
    return 0;
}