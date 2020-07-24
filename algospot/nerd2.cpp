#include <iostream>
#include <map>
using namespace std;

map<int,int> coords;

bool isdominated(int x,int y)
{
	map<int,int>::iterator it=coords.lower_bound(x);
	if(it==coords.end())return false;
	return y<it->second;
}

void removedominated(int x,int y)
{
	map<int,int>::iterator it=coords.lower_bound(x);
	if(it==coords.begin())return;
	it--;
	while(1)
	{
		if(it->second>y)break;
		if(it==coords.begin())
		{
			coords.erase(it);
			break;
		}
		else
		{
			map<int,int>::iterator jt=it;
			jt--;
			coords.erase(it);
			it=jt;
		}
	}
}

int registerd(int x,int y)
{
	if(isdominated(x,y))return coords.size();
	removedominated(x,y);
	coords[x]=y;
	return coords.size();
}

int main()
{
	int t,n,x,y,i,ret;
	cin>>t;
	while(t--)
	{
		cin>>n;
		ret=0;
		coords.clear();
		while(n--)
		{
			cin>>x>>y;
			ret+=registerd(x,y);
		}
		cout<<ret<<endl;
	}
	return 0;
}