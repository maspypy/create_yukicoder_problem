#include "testlib.h"
#include<bits/stdc++.h>
using namespace std;
using Int = long long;
const int MIN_N = 1;
const int MAX_N = 1000000;
const int MIN_MOD = 1;
const int MAX_MOD = 1000000007;
signed main(int argc,char* argv[]){
  registerValidation(argc, argv);
  inf.readInt(MIN_N, MAX_N, "N");
  inf.readSpace();
  inf.readInt(MIN_MOD, MAX_MOD, "MOD");
  inf.readEoln();
  inf.readEof();
  return 0;
}