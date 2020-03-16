#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

const int MOD = 1e9 + 7;

int sum_l[60000];
int sum_r[60000];
int A[150001];
int B[150001];
unordered_map<int, int> memo;

void calc_sums(int a[], int L, int R)
{
    int pow3 = 1;
    for (int i = L; i < R; i++)
    {
        int x = A[i];
        for (int j = 0; j < pow3; j++)
        {
            a[j + pow3] = a[j] + x;
            a[j + pow3 + pow3] = a[j] - x;
        }
        pow3 *= 3;
    }
}

pair<int, int> find_same_value(int lsize, int rsize)
{
    for (int i = 1; i < lsize; i++)
    {
        if (sum_l[i] == 0)
            return make_pair(i, 0);
    }
    for (int j = 1; j < rsize; j++)
    {
        if (sum_r[j] == 0)
            return make_pair(0, j);
    }
    for (int i = 1; i < lsize; i++)
    {
        memo[sum_l[i]] = i;
    }
    for (int j = 1; j < rsize; j++)
    {
        if (memo.find(sum_r[j]) != memo.end())
        {
            int i = memo[sum_r[j]];
            return make_pair(i, j);
        }
    }
    return make_pair(-1, -1);
};

int main()
{
    int N;
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        cin >> A[i];
    }
    int M = min(N, 20);
    int mid = M / 2;
    calc_sums(sum_l, 0, mid);
    calc_sums(sum_r, mid, M);
    int i, j;
    auto p = find_same_value(pow(3, mid), pow(3, M - mid));
    i = p.first;
    j = p.second;
    int coef[3] = {0, 1, -1};
    if (i == -1)
    {
        cout << "No" << endl;
    }
    else
    {
        int n = 0;
        while (i)
        {
            B[n] = coef[i % 3] * A[n];
            n++;
            i /= 3;
        }
        n = mid;
        while (j)
        {
            B[n] = -coef[j % 3] * A[n];
            n++;
            j /= 3;
        }
        cout << "Yes" << endl;
        for (int i = 0; i < N; i++)
        {
            if (i)
            {
                cout << " ";
            }
            cout << B[i];
        }
        cout << endl;
    }
    return 0;
}
