#include <iostream>
#include <cstring>
#include <algorithm>
#include <string>
using namespace std;

const int INF=987654321;
int cache[10000];
string num;

int getrank(int start,int end)
{
	string part=num.substr(start,end-start+1);
	if(part==string(part.size(),part[0]))
		return 1;
	bool progressive=true;
	for(int i=0,i<part.size();i++)
		if(part[i+1]-part[i]!=part[1]-part[0])
			progressive=false;
	if(progressive&&abs(part[1]-part[0])==1)
		return 2;
	bool alternate=true;
	for(int i=0;i<part.size();i++)
		if(part[i]!=part[i%2])
			alternate=false;
	if(alternate)
		return 4;
	if(progressive)
		return 5;
	return 10;
}

int solve(int idx)
{
	if(idx==num.size())
		return 0;
	int &result=cache[idx];
	if(result!=-1)
		return result;
	result=INF;
	for(int i=3;i<=5;i++)
		if(idx+i<=num.size())
			result=min(result,solve(idx+i)+getrank(idx,idx+i-1));
	return result;
}

void main()
{
	int test;
	cin>>test;
	while(test--)
	{
		memset(cache,-1,sizeof(cache));
		cin>>num;
		cout<<solve(0)<<endl<<endl;
	}
}


#include <stdio.h>
#include <string.h>

int D(char *c,int l)
{
	int i,d=c[1]-c[0];
	for(i=2;i<l&&c[i]-c[i-1]==d;i++);
	if(i==l)
		return (d==0)?1:(d==1||d==-1)?2:5;
	for(i=2;i<l&&c[i]-c[i-1]==(d=-d);i++);
	if(i==l)
		return 4;
	return 10;
}
int main()
{
	int C,L,i,j,t,d[10001];
	char n[10001];
	for(scanf("%d",&C);C--;)
	{
		scanf("%s",n);
		L=strlen(n);
		d[L]=0;
		for(i=L;--i>= 0;)
		{
			d[i]=1<<30;
			for(j=3;j<=5;j++)
			{
				if(i+j>L)
					break;
				t=d[i+j]+D(n+i,j);
				if(t<d[i]) 
					d[i]=t;
			}
		}
		printf("%d\n",*d);
	}
}