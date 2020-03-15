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

  int n;
  cin>>n;

  vector<int> as(n);
  for(int i=0;i<n;i++) cin>>as[i];

  int m=min(n,20);

  using P = pair<int, int>;
  vector<P> cnt;

  for(int b=1;b<(1<<m);b++){
    int sum=0;
    for(int i=0;i<m;i++)
      if((b>>i)&1) sum+=as[i];
    cnt.emplace_back(sum,b);
  }
  sort(cnt.begin(),cnt.end());

  for(int t=0;t+1<(int)cnt.size();t++){
    if(cnt[t+0].first!=cnt[t+1].first) continue;
    cout<<"Yes"<<endl;

    vector<int> xs(n,0);
    for(int i=0;i<m;i++){
      if((cnt[t+0].second>>i)&1) xs[i]=+1;
      if((cnt[t+1].second>>i)&1) xs[i]=-1;
    }

    for(int i=0;i<n;i++){
      if(i) cout<<" ";
      cout<<as[i]*xs[i];
    }
    cout<<endl;
    return 0;
  }

  cout<<"No"<<endl;
  return 0;
}
