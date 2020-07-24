#include <iostream>
#include <vector>
#include <cstring>
using namespace std;

int n,d,p,q;
double cache[51][101];
int connected[51][51],deg[51];

double search(int here,int days)
{
	if(days==0)return (here==p?1.0:0.0);
	double& ret=cache[here][days];
	if(ret!=-1)return ret;
	ret=0.0;
	for(int there=0;there<n;there++)
		if(connected[here][there])
			ret+=search(there,days-1)/deg[there];
	return ret;
}

int main()
{
	int test,i,j;
	cin>>test;
	while(test--)
	{
		cin>>n>>d>>p;
		for(i=0;i<n;i++)
			for(j=0;j<n;j++)
				cin>>connected[i][j];
		for(i=0;i<51;i++)
			for(j=0;j<101;j++)
				cache[i][j]=-1;
		memset(deg,0,sizeof(deg));
		for(i=0;i<n;i++)
			for(j=0;j<n;j++)
				deg[i]+=connected[i][j];
		cin>>q;
		vector<int> v;
		for(i=0;i<q;i++)
		{
			int there;
			cin>>there;
			v.push_back(there);
		}
		for(i=0;i<q;i++)
		{
			cout.precision(8);
			cout<<search(v[i],d)<<" ";
		}
		cout<<endl<<endl;
	}
}

#include<stdio.h>
int t,n,m,i,j,q,p,z,k,d[101],a;
double D[2][101],dd[101];
bool v[101][101];
int main()
{
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d%d%d",&n,&m,&p);
		for(i=0;i<n;i++)
			{
				d[i]=0;
				for(j=0;j<n;j++)
					{
						scanf("%d",&v[i][j]);
						d[i]+=v[i][j];
					}
			}
		for(i=0;i<n;i++)
			dd[i]=1.0/d[i],D[0][i]=D[1][i]=0.0;
		D[0][p]=1.0;
		z=1;
		for(i=0;i<m;i++)
		{
			for(j=0;j<n;j++)
				for(k=0;k<n;k++)
					if(v[j][k])
						D[z][k]+=dd[j]*D[1-z][j];
			for(j=0;j<n;j++)
				D[1-z][j]=0;
			z=1-z;
		}
		scanf("%d",&q);
		while(q--)
			{
				scanf("%d",&a);
				printf("%.8lf ",D[1-z][a]);
			}
		printf("\n");
	}
}