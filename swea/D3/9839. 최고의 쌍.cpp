#include <bits/stdc++.h>
using namespace std;

int board[1000], ans, n;

void sol(int idx, int next)
{
    if(next == n) return;
    int tmp = board[idx] * board[next];
    int save = tmp;
    int a = tmp%10;
    bool chk = true;
    tmp/=10;
    while(tmp)
    {
        int b = tmp%10;
        if(a-b!=1)
        {
            chk = false;
            break;
        }
        a = b;
        tmp/=10;
    }
    if(ans<save&&chk) ans=save;
    sol(idx,next+1);
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int t;
    cin >> t;
    for(int tc=1;tc<=t;tc++)
    {
        ans=-1;
        cin>>n;
        for(int i=0;i<n;i++)
            cin>>board[i];
        for(int i=0;i<n-1;i++)
            sol(i,i+1);
        cout<<'#'<<tc<<' '<<ans<<endl;
    }
    return 0;
}