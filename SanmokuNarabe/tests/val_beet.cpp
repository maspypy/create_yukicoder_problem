#include "testlib.h"
#include <bits/stdc++.h>
using namespace std;

const int MIN_T = 1;
const int MAX_T = 100;

const int MIN_N = 1;
const int MAX_N = 1000;

void input() {
  int T = inf.readInt(MIN_T, MAX_T, "T");
  inf.readEoln();
  for(int i=0;i<T;i++){
    int N = inf.readInt(MIN_N, MAX_N, "N");
    inf.readSpace();
    string S = inf.readToken(format("[ox-]{%d}",N),"S");
    inf.readEoln();
    int O = count(S.begin(), S.end(), 'o');
    int X = count(S.begin(), S.end(), 'x');
    ensure(O == X);
  }
  inf.readEof();
}

int main() {
  registerValidation();
  input();
  return 0;
}
