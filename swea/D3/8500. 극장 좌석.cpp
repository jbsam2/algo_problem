#include <bits/stdc++.h>
using namespace std;

bool desc(int a, int b){ return a > b; }
int main()
{
    int tc;
    cin>>tc;
    for(int t=1;t<=tc;t++)
    {
        int n;
        cin>>n;
        vector<int> input;
        for(int i=0;i<n;i++)
        {
            int tmp;
            cin>>tmp;
            input.push_back(tmp);
        }
        sort(input.begin(), input.end(),desc);
        int ans = 2*input[0]+1;
        for(int i=1;i<input.size();i++)
            ans += 1+input[i];
        cout<<'#'<<t<<' '<<ans<<endl;
    }
}