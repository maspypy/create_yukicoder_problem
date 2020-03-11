#include "testlib.h"
#include <bits/stdc++.h>
using namespace std;
using Int = long long;
const Int MIN_N = 1;
const Int MAX_N = 1e5;
const Int MIN_X = 0;
const Int MAX_X = 1e9;
const Int MIN_Y = 0;
const Int MAX_Y = 1e9;
const Int MIN_Z = 0;
const Int MAX_Z = 1e9;
const Int MIN_A = 1;
const Int MAX_A = 1e9;

signed main(int argc, char *argv[])
{
    registerValidation(argc, argv);
    int N = inf.readLong(MIN_N, MAX_N, "N");
    inf.readSpace();
    int X = inf.readLong(MIN_X, MAX_X, "X");
    inf.readSpace();
    int Y = inf.readLong(MIN_Y, MAX_Y, "Y");
    inf.readSpace();
    int Z = inf.readLong(MIN_Z, MAX_Z, "Z");
    inf.readEoln();
    for (int i = 0; i < N; i++)
    {
        if (i)
        {
            inf.readSpace();
        }
        inf.readLong(MIN_A, MAX_A, "A");
    }
    inf.readEoln();
    inf.readEof();
    return 0;
}
