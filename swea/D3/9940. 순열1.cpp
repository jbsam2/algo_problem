#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin>>t;
    for(int tc=1;tc<=t;tc++)
    {
        int n;
        cin>>n;
        string ret;
        ret = "Yes";
        int arr[n];
        for(int i=0;i<n;i++)
            cin>>arr[i];
        sort(arr,arr+n);
        for(int i=0;i<n;i++)
        {
            if(arr[i] != i+1)
            {
                ret = "No";
                break;
            }
        }
        cout<<'#'<<tc<<' '<<ret<<endl;
    }
}