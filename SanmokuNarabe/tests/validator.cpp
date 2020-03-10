#include "testlib.h"
#include <bits/stdc++.h>
using namespace std;
using Int = long long;
const Int MIN_N = 1;
const Int MAX_N = 1e5;

signed main(int argc, char *argv[])
{
    registerValidation(argc, argv);
    int N = inf.readLong(MIN_N, MAX_N, "N");
    inf.readEoln();
    int o = 0;
    int x = 0;
    for (int i = 0; i < N; i++)
    {
        char c = inf.readChar();
        if(c == 'o')
            o++;
        if(c == 'x')
            x++;
        ensuref(c == 'o' || c == 'x' || c == '-', "Only o, x, - is allowed.");
    }
    ensuref(o == x, "The number of o and x must be equal.");
    inf.readEoln();
    inf.readEof();
    return 0;
}
