#include <bits/stdc++.h>
using namespace std;

int main()
{
	int tc;
    cin>>tc;
	for (int t=1;t<=tc;t++)
	{
		int n, b, e, tmp, c=0, r;
		cin>>n>>b>>e;
		for (int i=0;i<n;i++)
        {
			scanf("%d", &tmp);
			r = (b/tmp-1)*tmp;
			for (int j=0;j<3;j++)
            {
				if ((r <=(b+e)) && ((b-e)<=r)) 
                { 
                    c++;
                    break;
                }
                r+=tmp;
			}
		}
		printf("#%d %d\n", t, c);
	}
	return 0;
}