#include <iostream>
using namespace std;

int abs(int num)
{
    if (num<0)
        return -num;
    else if (num>0)
        return num;
    else
        return 0;
}

int main()
{
    int t;
    cin>>t;
    for(int tc=1;tc<=t;tc++)
    {
        int n;
        int cnt = 0, min = 987654321;
        cin>>n;
        for(int i=0;i<n;i++)
        {
            int tmp;
            cin>>tmp;
            if( abs(tmp) < min )
            {
                min = abs(tmp);
                cnt = 1;
            }
            else if (abs(tmp) == min)
                cnt++;
        }
        printf("#%d %d %d\n",tc,min,cnt);
    }
}