#include "testlib.h"
#include <bits/stdc++.h>
using namespace std;

using ll = long long;

const ll MIN_N = 1;
const ll MAX_N = 1e5;

const ll MIN_M = 1;
const ll MAX_M = 1e9;

const ll MIN_Q = 1;
const ll MAX_Q = 1e5;

const ll MIN_S = 1;
const ll MAX_S = 1e5;

void input() {
  ll N = inf.readLong(MIN_N, MAX_N, "N");
  inf.readSpace();
  ll M = inf.readLong(MIN_M, MAX_M, "M");
  inf.readSpace();
  ll Q = inf.readLong(MIN_Q, min(N * M, MAX_Q), "Q");
  inf.readEoln();

  string S = inf.readString();
  for (char c : S)
    ensure(islower(c));
  inf.readEoln();

  ll last = 0;
  for (int i = 0; i < Q; i++) {
    if (i)
      inf.readSpace();
    ll K = inf.readLong(last + 1, N * M, "K");
    last = K;
  }
  inf.readEoln();

  inf.readEof();
}

int main() {
  registerValidation();
  input();
  return 0;
}
