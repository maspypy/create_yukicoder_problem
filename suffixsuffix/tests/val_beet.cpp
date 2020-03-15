#include "testlib.h"
#include <bits/stdc++.h>
using namespace std;

using ll = long long;

const ll MIN_S = 1;
const ll MAX_S = 1e5;

const ll MIN_N = 1;
const ll MAX_N = 1e9;

const ll MIN_K = 1;

void input() {
  string S = inf.readString();
  for(char c: S) ensure(islower(c));
  ll N = inf.readLong(MIN_N, MAX_N, "N");
  inf.readSpace();
  inf.readLong(MIN_K, N * (ll)S.size(), "K");
  inf.readEoln();
  inf.readEof();
}

int main() {
  registerValidation();
  input();
  return 0;
}
