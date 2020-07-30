#include <iostream>
#include <string>
using namespace std;

int main()
{
    int tc;
    cin>>tc;
    for(int t=1;t<=tc;t++)
    {
        int max = 0;
        int min = 987654321;
        for(int i=0;i<10;i++)
        {
            int total = 0;
            int tmp;
            cin>>tmp;
            
            while(tmp>0)
            {
                total += (tmp%10);
                tmp /= 10;
            }
            if(total>max)
                max=total;
            if(total<min)
                min=total;
        }
        cout<<'#'<<t<<' '<<max<<' '<<min<<endl;
    }
}