#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin>>t;
    for(int tc=1;tc<=t;tc++)
    {
        int time;
        cin>>time;
        int hour = time/30;
        int min = (time%30)*2;
        cout<<"#"<<tc<<" "<<hour<<" "<<min<<endl;
    }
}