#include <bits/stdc++.h>
using namespace std;
template<typename T1,typename T2> inline void chmin(T1 &a,T2 b){if(a>b) a=b;}
template<typename T1,typename T2> inline void chmax(T1 &a,T2 b){if(a<b) a=b;}
using Int = long long;
const char newl = '\n';

//INSERT ABOVE HERE
signed main(){
  cin.tie(0);
  ios::sync_with_stdio(0);

  int n,x,y,z;
  cin>>n>>x>>y>>z;

  vector<int> as(n);
  for(int i=0;i<n;i++) cin>>as[i];

  for(int i=0;i<n;i++){
    as[i]/=1000;
    as[i]++;
    as[i]*=1000;
  }

  vector<int> cs({10000,5000,1000});
  vector<int> vs({z,y,x});
  for(int t=0;t<3;t++){
    int c=cs[t],v=vs[t];
    for(int i=0;i<n;i++){
      int k=min(as[i]/c,v);
      as[i]-=c*k;
      v-=k;
    }
    sort(as.rbegin(),as.rend());
    for(int i=0;i<min(n,v);i++) as[i]=0;
  }

  if(as==vector<int>(n,0)) cout<<"Yes"<<endl;
  else cout<<"No"<<endl;

  return 0;
}
