#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define MAX 1000010
const int MOD = 998244353;

bool is_prime[MAX];
ll mu[MAX];

vector<int> prime_table()
{
    is_prime[2] = true;
    for (int n = 3; n < MAX; n += 2)
    {
        is_prime[n] = true;
    }
    for (int p = 3; p * p < MAX; p += 2)
    {
        if (is_prime[p])
        {
            int q = p * p;
            for (int i = q; i < MAX; i += p)
            {
                is_prime[i] = false;
            }
        }
    }
    vector<int> primes;
    for (int p = 0; p < MAX; p++)
    {
        if (is_prime[p])
        {
            primes.emplace_back(p);
        }
    }
    return primes;
}

void mobius_table(vector<int> primes)
{
    for (int n = 1; n < MAX; n++)
    {
        mu[n] = 1;
    }
    for (int i = 0; i < primes.size(); i++)
    {
        ll p = primes[i];
        for (int j = p; j < MAX; j += p)
        {
            mu[j] *= (-1);
        }
        ll q = p * p;
        if (q >= MAX)
            continue;
        for (int j = q; j < MAX; j += q)
        {
            mu[j] = 0;
        }
    }
}

ll F(ll N)
{
    ll x_max = sqrt(N);
    ll S = 0;
    for (ll x = 1; x <= x_max; x++)
    {
        ll y_max = sqrt(N - x * x);
        S += x * (1 + 2 * y_max);
        S %= MOD;
    }
    return S;
}

ll f(ll N)
{
    ll ret = 0;
    for (ll d = 1; d <= N; d++)
    {
        ll n = N / (d * d);
        if (n == 0)
        {
            break;
        }
        ret += F(n) * mu[d] * d % MOD;
    }
    ret %= MOD;
    ret *= 24;
    ret -= 16;
    ret %= MOD;
    if (ret < 0)
        ret += MOD;
    return ret;
}

int main()
{
    ll N;
    cin >> N;
    vector<int> primes = prime_table();
    mobius_table(primes);
    cout << f(N) << endl;
    return 0;
}
