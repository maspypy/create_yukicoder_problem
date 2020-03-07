#include "testlib.h"
#include<bits/stdc++.h>
using namespace std;
using Int = long long;
const int MIN_A = 1;
const int MAX_A = 1000;
const int MIN_B = 1;
const int MAX_B = 1000;
signed main(int argc,char* argv[]){
  registerValidation(argc, argv);
  inf.readInt(MIN_A, MAX_A, "A");
  inf.readEoln();
  inf.readInt(MIN_B, MAX_B, "B");
  inf.readEoln();
  inf.readEof();
  return 0;
}