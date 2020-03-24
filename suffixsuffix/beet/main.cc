#include <bits/stdc++.h>
using namespace std;
template<typename T1,typename T2> inline void chmin(T1 &a,T2 b){if(a>b) a=b;}
template<typename T1,typename T2> inline void chmax(T1 &a,T2 b){if(a<b) a=b;}
using Int = long long;
const char newl = '\n';

// longest common prefix of s and s[i:n]
template<typename T>
vector<int> zalgorithm(vector<T> vs){
  int n=vs.size();
  vector<int> as(n+1,0);
  as[0]=n;
  int i=1,j=0;
  while(i<n){
    while(i+j<n&&vs[j]==vs[i+j]) j++;
    as[i]=j;
    if(j==0){
      i++;
      continue;
    }
    int k=1;
    while(i+k<n&&k+as[k]<j) as[i+k]=as[k],k++;
    i+=k;
    j-=k;
  }
  return as;
}
vector<int> zalgorithm(string s){
  return zalgorithm(vector<char>(s.begin(),s.end()));
}

struct SuffixArray{
  string s;
  vector<int> sa,rev;

  SuffixArray(){}
  SuffixArray(const string &S):s(S){
    int n=s.size();
    s.push_back('$');
    sa.resize(n+1);
    iota(sa.begin(),sa.end(),0);
    sort(sa.begin(),sa.end(),
         [&](int a,int b){
           if(s[a]==s[b]) return a>b;
           return s[a]<s[b];
         });
    vector<int> cs(n+1,0),rs(n+1),cnt(n+1);
    for(int i=0;i<=n;i++) rs[i]=s[i];
    for(int len=1;len<=n;len*=2){
      for(int i=0;i<=n;i++){
        cs[sa[i]]=i;
        if(i>0 &&
           rs[sa[i-1]]==rs[sa[i]] &&
           sa[i-1]+len<=n &&
           rs[sa[i-1]+len/2]==rs[sa[i]+len/2]) cs[sa[i]]=cs[sa[i-1]];
      }
      iota(cnt.begin(),cnt.end(),0);
      copy(sa.begin(),sa.end(),rs.begin());
      for(int i=0;i<=n;i++){
        int s1=rs[i]-len;
        if(s1>=0) sa[cnt[cs[s1]]++]=s1;
      }
      cs.swap(rs);
    }
    rev.resize(n+1);
    for(int i=0;i<=n;i++) rev[sa[i]]=i;
  }
  int operator[](int i) const{return sa[i];}

  bool lt_substr(string &t,int si,int ti){
    int sn=s.size(),tn=t.size();
    while(si<sn&&ti<tn){
      if(s[si]<t[ti]) return 1;
      if(s[si]>t[ti]) return 0;
      si++;ti++;
    }
    return si==sn&&ti<tn;
  }

  int lower_bound(string& t){
    int l=0,r=s.size();
    while(l+1<r){
      int m=(l+r)>>1;
      if(lt_substr(t,sa[m],0)) l=m;
      else r=m;
    }
    return r;
  }

  int upper_bound(string& t){
    t.back()++;
    int res=lower_bound(t);
    t.back()--;
    return res;
  }

  // O(|T|*log|S|)
  int count(string& T){
    return upper_bound(T)-lower_bound(T);
  }
};

//INSERT ABOVE HERE
signed main(){
  cin.tie(0);
  ios::sync_with_stdio(0);

  using ll = long long;
  ll n,m,q;
  cin>>n>>m>>q;

  string s;
  cin>>s;

  vector<ll> ks(q);
  for(int i=0;i<q;i++) cin>>ks[i];

  auto zs=zalgorithm(s+s);
  for(int i=1;i<=n;i++){
    if(n%i) continue;
    if(zs[i]>=n){
      m*=n/i;
      s=s.substr(0,i);
      break;
    }
  }
  n=s.size();

  if(n==1){
    for(int i=0;i<q;i++){
      if(i) cout<<" ";
      cout<<m-ks[i]+1;
    }
    cout<<endl;
    return 0;
  }

  if(m==1){
    SuffixArray sa(s);
    for(int i=0;i<q;i++){
      if(i) cout<<" ";
      cout<<1+sa.sa[ks[i]];
    }
    cout<<endl;
    return 0;
  }

  SuffixArray sa(s+s);
  vector<ll> ans(q,-1);

  ll tmp=0;
  for(int i=1,j=0;i<=n*2;i++){
    if(sa.sa[i]>=n){
      tmp++;
      if(j<q and ks[j]==tmp){
        ans[j]=n*(m-2)+1+sa.sa[i];
        j++;
      }
    }else{
      tmp+=m-1;
      while(j<q and ks[j]<=tmp){
        ans[j]=1+sa.sa[i]-(ks[j]-tmp)*n;
        j++;
      }
    }
  }

  for(int i=0;i<q;i++){
    if(i) cout<<" ";
    cout<<ans[i];
  }
  cout<<endl;
  return 0;
}
