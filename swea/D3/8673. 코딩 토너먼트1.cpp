#include <bits/stdc++.h>
using namespace std;

vector<int> vnow, vnext;

int getret()
{
    int ret = 0;
    while(1)
    {
        vnow=vnext;
        vnext.clear();
        for(int i=0;i<vnow.size();i+=2)
        {
            vnow[i] >= vnow[i+1] ? vnext.emplace_back(vnow[i]):vnext.emplace_back(vnow[i+1]);
            ret += abs(vnow[i]-vnow[i+1]);
        }
        if(vnext.size() == 1)
            return ret;
    }
}

int main()
{
    int tc;
    cin>>tc;
    for(int t=1;t<=tc;t++)
    {
        vnow.clear();
        vnext.clear();
        int k;
        cin>>k;
        for(int i=0;i<pow(2,k);i++)
        {
            int tmp;
            cin>>tmp;
            vnext.push_back(tmp);
        }
        cout<<'#'<<t<<' '<<getret()<<endl;
    }
}