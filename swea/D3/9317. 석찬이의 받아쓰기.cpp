#include <bits/stdc++.h>
using namespace std;

int main()
{
    int tc;
    cin>>tc;
    for(int t=1;t<=tc;t++)
    {
        int n;
        cin>>n;
        string s1,s2;
        cin>>s1>>s2;
        int cnt = 0;
        for(int i=0;i<n;i++)
            if(s1[i] == s2[i])
                cnt++;
        cout<<'#'<<t<<' '<<cnt<<endl;
    }
}