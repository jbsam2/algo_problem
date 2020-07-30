#include <bits/stdc++.h>
using namespace std;

int main()
{
    int cards[12];
    int tc;
    cin>>tc;
    for(int t=1;t<=tc;t++)
    {
        int n;
        cin>>n;
        int now_sum = 0, less = 0, over = 0;
        for(int i=2;i<=11;i++)
            cards[i]=4;
        cards[10]=16;
        
        int tmp;
        for(int i=0;i<n;i++)
        {
            cin>>tmp;
            cards[tmp]--;
            now_sum += tmp;
        }
        int left = 21 - now_sum;
        for(int i=2;i<=left;i++)
            less += cards[i];
        for(int i=left+1;i<=11;i++)
            over += cards[i];
        if(over>less)
            cout<<'#'<<t<<" STOP"<<endl;
        else
            cout<<'#'<<t<<" GAZUA"<<endl;
    }
    return 0;
}