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

  string s;
  cin>>s;

  using ll = long long;
  ll n,k;
  cin>>n>>k;

  auto zs=zalgorithm(s+s);
  for(int i=1;i<=(int)s.size();i++){
    if(s.size()%i) continue;
    if(zs[i]>=(int)s.size()){
      n*=s.size()/i;
      s=s.substr(0,i);
      break;
    }
  }

  if(s.size()==1){
    cout<<n-k+1<<endl;
    return 0;
  }

  if(n==1){
    SuffixArray sa(s);
    int v=sa.sa[1+(k-1)/n];
    cout<<1+v<<endl;
    return 0;
  }

  SuffixArray sa(s+s);
  for(int i=1;i<=(int)s.size()*2;i++){
    if(sa.sa[i]>=(int)s.size()){
      k--;
      if(k==0){
        cout<<(int)s.size()*(n-2)+1+sa.sa[i]<<endl;
        break;
      }
    }else{
      k-=n-1;
      if(k<=0){
        ll ans=1+sa.sa[i];
        ans-=k*(int)s.size();
        cout<<ans<<endl;
        break;
      }
    }
  }
  return 0;
}
