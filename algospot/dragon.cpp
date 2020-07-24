#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

const int MAX=1000000001;
const string EXPAND_X="X+YF";
const string EXPAND_Y="FX-Y";
int length[51];

void precal()
{
	length[0]=1;
	for(int i=1;i<51;i++)
		length[i]=min(MAX,2*length[i-1]+2);
}

char expand(const string& dragoncurve,int gen,int skip)
{
	if(gen==0)
	{
		if(skip>dragoncurve.size())
			exit(-1);
		return dragoncurve[skip];
	}
	for(int i=0;i<dragoncurve.size();i++)
	{
		if(dragoncurve[i]=='X'||dragoncurve[i]=='Y')
		{
			if(skip>=length[gen])
				skip-=length[gen];
			else if(dragoncurve[i]=='X')
				return expand(EXPAND_X,gen-1,skip);
			else
				return expand(EXPAND_Y,gen-1,skip);
		}
		else if(skip>0)
			skip--;
		else
			return dragoncurve[i];
	}
}

int main()
{
	int test;
	cin>>test;
	precal();
	while(test--)
	{
		int gen,skip,range;
		cin>>gen>>skip>>range;
		for(int i=0;i<range;i++)
			cout<<expand("FX",gen,skip+i-1);
		cout<<endl;
	}
	return 0;
}

#include<cstdio>
int main()
{
	int n,m,i;
	scanf("%d");
	while(~scanf("%d%d%d",&i,&n,&m))
		for(puts("");m--;n++)
			putchar("+FX-YF"[n%3?n%6:n/3&-n/3&n/6?3:0]);
}

#include <iostream>
using namespace std;
int p,l,o,c;
int main()
{
    cin>>c;
	for(;c--;)
	{
		cin>>p>>p>>l;
		int i=p-1;
		while(++i<p+l)
			if(i%3)
				cout<<"FX YF"[i%6-1];
			else
			{
				o=i/3;
				while(o%2==0)
					o/=2;
				cout<<"+-"[o%4/2];				
			}
		cout<<endl;
	}
}