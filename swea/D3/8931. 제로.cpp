#include <bits/stdc++.h>
using namespace std;

int main()
{
    int tc;
    cin>>tc;
    for(int t=1;t<=tc;t++)
    {
        int k;
        cin>>k;
        stack<int> ans;
        int ret=0;
        for(int i=0;i<k;i++)
        {
            int tmp;
            cin>>tmp;
            if (tmp)
                ans.push(tmp);
            else
            {
                if(ans.empty()) ans.push(tmp);
                else ans.pop();
            }
        }
        while(ans.size())
        {
            ret += ans.top();
            ans.pop();
        }
        cout<<'#'<<t<<' '<<ret<<endl;
    }
}