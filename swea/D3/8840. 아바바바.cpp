#include <bits/stdc++.h>
using namespace std;

int main()
{
    int tc;
    scanf("%d",&tc);
    for(int t=1;t<=tc;t++)
    {
        long long n;
        scanf("%lld",&n);
        long long m = n/2;
        printf("#%lld %lld\n",t, m*m);
    }
    return 0;
}