#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin>>t;
    for(int tc=1;tc<=t;tc++)
    {
        int n, k;
        cin>>n>>k;
        if(n%k)
            printf("#%d 1\n",tc);
        else
            printf("#%d 0\n",tc);
    }
}