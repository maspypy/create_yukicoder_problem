#include <bits/stdc++.h>
using namespace std;
template<typename T1,typename T2> inline void chmin(T1 &a,T2 b){if(a>b) a=b;}
template<typename T1,typename T2> inline void chmax(T1 &a,T2 b){if(a<b) a=b;}
using Int = long long;
const char newl = '\n';

vector<string> split(string& s,char c){
  int n=s.size();
  vector<string> res;
  for(int i=0;i<n;i++){
    if(s[i]==c) continue;
    string t;
    while(i<n&&s[i]!=c) t.push_back(s[i++]);
    res.push_back(t);
  }
  return res;
}

signed solve(){
  int n;
  cin>>n;
  string s;
  cin>>s;

  vector<string> wins({"ooo","oo-","o-o","-oo","-o--","--o-"});

  for(string w:wins){
    if(s.find(w)!=string::npos){
      cout<<"O\n";
      return 0;
    }
  }

  auto ss=split(s,'x');
  for(string t:ss){
    if(t.size()<3) continue;
    if(t.front()!='o'||t.back()!='o') continue;
    if(t.size()&1){
      cout<<"O\n";
      return 0;
    }
  }

  cout<<"X\n";
  return 0;
}

//INSERT ABOVE HERE
signed main(){
  cin.tie(0);
  ios::sync_with_stdio(0);

  int T;
  cin>>T;
  while(T--) solve();

  return 0;
}
