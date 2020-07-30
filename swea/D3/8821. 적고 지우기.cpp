#include <string>
#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int tc,n,tmp,start;
    string ans = "";
    cin>>tc;
    for(int t=1;t<=tc;t++)
    {
        n=0;
        string input;
        cin>>input;
        sort(input.begin(), input.end());
        for(int i=0;i<input.size();i++)
        {
            tmp=0;
            start=i;
            while(input[i]==input[start])
            {
                tmp++;
                i++;
            }
            if(tmp%2!=0)
                n++;
            i--;
        }
        printf("#%d %d\n",t,n);
    }
}