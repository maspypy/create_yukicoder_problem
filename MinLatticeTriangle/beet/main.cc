#include <bits/stdc++.h>
using namespace std;
template <typename T1, typename T2>
inline void chmin(T1 &a, T2 b)
{
  if (a > b)
    a = b;
}
template <typename T1, typename T2>
inline void chmax(T1 &a, T2 b)
{
  if (a < b)
    a = b;
}
using Int = long long;
const char newl = '\n';

template <typename T, T MOD = 998244353>
struct Mint
{
  static constexpr T mod = MOD;
  T v;
  Mint() : v(0) {}
  Mint(signed v) : v(v) {}
  Mint(long long t)
  {
    v = t % MOD;
    if (v < 0)
      v += MOD;
  }

  Mint pow(long long k)
  {
    Mint res(1), tmp(v);
    while (k)
    {
      if (k & 1)
        res *= tmp;
      tmp *= tmp;
      k >>= 1;
    }
    return res;
  }

  static Mint add_identity() { return Mint(0); }
  static Mint mul_identity() { return Mint(1); }

  Mint inv() { return pow(MOD - 2); }

  Mint &operator+=(Mint a)
  {
    v += a.v;
    if (v >= MOD)
      v -= MOD;
    return *this;
  }
  Mint &operator-=(Mint a)
  {
    v += MOD - a.v;
    if (v >= MOD)
      v -= MOD;
    return *this;
  }
  Mint &operator*=(Mint a)
  {
    v = 1LL * v * a.v % MOD;
    return *this;
  }
  Mint &operator/=(Mint a) { return (*this) *= a.inv(); }

  Mint operator+(Mint a) const { return Mint(v) += a; }
  Mint operator-(Mint a) const { return Mint(v) -= a; }
  Mint operator*(Mint a) const { return Mint(v) *= a; }
  Mint operator/(Mint a) const { return Mint(v) /= a; }

  Mint operator-() const { return v ? Mint(MOD - v) : Mint(v); }

  bool operator==(const Mint a) const { return v == a.v; }
  bool operator!=(const Mint a) const { return v != a.v; }
  bool operator<(const Mint a) const { return v < a.v; }

  static Mint comb(long long n, int k)
  {
    Mint num(1), dom(1);
    for (int i = 0; i < k; i++)
    {
      num *= Mint(n - i);
      dom *= Mint(i + 1);
    }
    return num / dom;
  }
};
template <typename T, T MOD>
constexpr T Mint<T, MOD>::mod;
template <typename T, T MOD>
ostream &operator<<(ostream &os, Mint<T, MOD> m)
{
  os << m.v;
  return os;
}

//INSERT ABOVE HERE
const int MAX = 1e6 + 10;
vector<int> dp[MAX];

using ll = long long;
ll naive(ll n)
{
  ll ans = 0;
  for (ll p1 = -n; p1 <= n; p1++)
  {
    for (ll p2 = -n; p2 <= n; p2++)
    {
      for (ll q1 = -n; q1 <= n; q1++)
      {
        for (ll q2 = -n; q2 <= n; q2++)
        {
          if (p1 * p1 + p2 * p2 > n)
            continue;
          if (q1 * q1 + q2 * q2 > n)
            continue;
          if (p1 * q2 - p2 * q1 != 1)
            continue;
          ans += abs(p1) + abs(p2) + abs(q1) + abs(q2);
        }
      }
    }
  }
  return ans;
}

signed main()
{
  cin.tie(0);
  ios::sync_with_stdio(0);

  using ll = long long;
  ll n;
  cin >> n;

  // cout<<naive(n)<<endl;

  for (ll i = 2; i < MAX; i++)
  {
    if (!dp[i].empty())
      continue;
    for (ll j = i; j < MAX; j += i)
      dp[j].emplace_back(i);
  }

  using M = Mint<int, 998244353>;
  M ans{0};

  for (ll i = 1; i * i <= n; i++)
  {
    ll j = sqrtl(n - i * i);
    while (i * i + (j + 1) * (j + 1) <= n)
      j++;
    while (i * i + j * j > n)
      j--;

    ll m = dp[i].size();
    ll s = 1 << m;
    ll cnt = 0;
    for (ll b = 0; b < s; b++)
    {
      ll prod = 1;
      for (ll k = 0; k < m; k++)
        if ((b >> k) & 1)
          prod *= dp[i][k];
      if (__builtin_parity(b))
        cnt -= j / prod;
      else
        cnt += j / prod;
    }

    ans += M(i * 4) * M(6) * M(cnt);
  }

  ans *= M(2);
  ans += M(8);
  cout << ans << newl;
  return 0;
}
