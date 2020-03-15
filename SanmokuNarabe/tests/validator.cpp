#include "testlib.h"
#include <bits/stdc++.h>
using namespace std;
using Int = long long;
const Int MIN_N = 1;
const Int MAX_N = 1000;
const Int MIN_T = 1;
const Int MAX_T = 100;

signed main(int argc, char *argv[])
{
    registerValidation(argc, argv);
    int T = inf.readLong(MIN_T, MAX_T, "T");
    inf.readEoln();
    for (int t = 0; t < T; t++)
    {
        int N = inf.readLong(MIN_N, MAX_N, "N");
        inf.readSpace();
        int o = 0;
        int x = 0;
        for (int i = 0; i < N; i++)
        {
            char c = inf.readChar();
            if (c == 'o')
                o++;
            if (c == 'x')
                x++;
            ensuref(c == 'o' || c == 'x' || c == '-', "Only o, x, - is allowed.");
        }
        ensuref(o == x, "The number of o and x must be equal.");
        inf.readEoln();
    }
    inf.readEof();
    return 0;
}
