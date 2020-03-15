#include "testlib.h"
#include <bits/stdc++.h>
using namespace std;

const int MIN_N = 1;
const int MAX_N = 150000;

const int MIN_A = 1;
const int MAX_A = 150000;

void input() {
  int N = inf.readInt(MIN_N, MAX_N, "N");
  inf.readEoln();
  vector<int> A(N);
  for (int i = 0; i < N; i++) {
    if (i)
      inf.readSpace();
    A[i] = inf.readInt(MIN_A, MAX_A, "A");
  }
  inf.readEoln();
  inf.readEof();
}

int main() {
  registerValidation();
  input();
  return 0;
}
