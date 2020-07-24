#include <iostream>
#include <vector>
#include <string>
#include <cmath>
using namespace std;

vector<int> v;

int main()
{
	int ans=0,cnt=-1,i;
	v.clear();
	string dart;
	cin>>dart;
	for(i=0;i<dart.size();i++)
	{
		char tmp=dart[i];
		if(tmp>='0'&&tmp<='9')
		{
			cnt++;
			v.push_back(tmp-'0');
			if(tmp=='1'&&dart[i+1]=='0')
			{
				v[cnt]=10;
				i++;
			}
		}
		else if(tmp=='D')v[cnt]*=v[cnt];
		else if(tmp=='T')v[cnt]=pow(v[cnt],3);
		else if(tmp=='*')v[cnt]*=2,v[cnt-1]*=2;
		else if(tmp=='#')v[cnt]*=-1;
	}
	for(i=0;i<3;i++)ans+=v[i];
	cout<<ans;
	return 0;
}