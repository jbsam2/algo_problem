#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

const int INF=987654321;
int n,k,m,l,prerequisite[12],classes[10],cache[10][1<<12];
int bitcount(int n)
{
	if(n==0)
		return 0;
	return n%2+bitcount(n/2);
}

int graduate(int semester,int taken)
{
	if(bitcount(taken)>=k)return 0;
	if(semester==m)return INF;
	int &ret=cache[semester][taken];
	if(ret!=-1)return ret;
	ret=INF;
	int cantake=(classes[semester]&~taken);
	for(int i=0;i<n;i++)
		if((cantake&(1<<i))&&(taken&prerequisite[i])!=prerequisite[i])
			cantake&=~(1<<i);
	for(int take=cantake;take>0;take=((take-1)&cantake))
	{
		if(bitcount(take)>l)continue;
		ret=min(ret,graduate(semester+1,taken|take)+1);
	}
	ret=min(ret,graduate(semester+1,taken));
	return ret;
}

int main()
{
	int t,tmp,subject,ret;
	cin>>t;
	while(t--)
	{
		memset(prerequisite,0,sizeof(prerequisite));
		memset(classes,0,sizeof(classes));
		memset(cache,-1,sizeof(cache));
		cin>>n>>k>>m>>l;
		for(int i=0;i<n;i++)
		{
			cin>>tmp;
			while(tmp--)
			{
				cin>>subject;
				prerequisite[i]|=(1<<subject);
			}
		}
		for(int i=0;i<m;i++)
		{
			cin>>tmp;
			while(tmp--)
			{
				cin>>subject;
				classes[i]|=(1<<subject);
			}
		}
		ret=graduate(0,0);
		if(ret==INF)
			cout<<"IMPOSSIBLE"<<endl;
		else
			cout<<ret<<endl;
	}
	return 0;
}