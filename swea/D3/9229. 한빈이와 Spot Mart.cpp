#include <bits/stdc++.h>
using namespace std;

int main()
{
    int tc;
    cin>>tc;
    for(int t=1;t<=tc;t++)
    {
        int n,m,ans=-1;
        cin>>n>>m;
        int snack[n];
        for(int i=0;i<n;i++)
            cin>>snack[i];
        for(int i=0;i<n;i++)
        {
            for(int j=i+1;j<n;j++)
            {
                int tmp=snack[i]+snack[j];
                if(tmp>ans && tmp<=m)
                    ans = tmp;
            }
        }
        cout<<'#'<<t<<' '<<ans<<endl;
    }
}