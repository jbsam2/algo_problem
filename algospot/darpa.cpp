#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>
using namespace std;

bool decision(const vector<double>& location,int cam,double gap)
{
	double lim=-1;
	int installed=0;
	for(int i=0;i<location.size();i++)
	{
		if(lim<=location[i])
		{
			installed++;
			lim=location[i]+gap;
		}
	}
	return installed>=cam;
}

double opt(const vector<double>& location,int cam)
{
	double low=0,hi=241;
	for(int i=0;i<100;i++)
	{
		double mid=(low+hi)/2.0;
		if(decision(location,cam,mid))low=mid;
		else hi=mid;
	}
	return low;
}

int main()
{
	int test,camera,install;
	cin>>test;
	while(test--)
	{
		vector<double> v;
		cin>>camera>>install;
		while(install--)
		{
			double c;
			cin>>c;
			v.push_back(c);
		}
		sort(v.begin(),v.end());
		cout<<fixed<<setprecision(2);
		cout<<opt(v,camera)<<endl;
	}
	return 0;
}

#include<cstdio>
int T,n,m;
double inp[210];
int main()
{
	int i,j;
	double l,r,md,lst;
	for(scanf("%d",&T); T--;)
	{
		scanf("%d%d",&n,&m);
		for(i=0; i<m; i++)
			scanf("%lf",&inp[i]);
		l=0; r=241;
		while(r-l>0.001)
		{
			md=(l+r)/2.;
			j=1; lst=inp[0]+md;
			for(i=1; i<m&&j<n; i++)
			{
				if(inp[i]>=lst)
				{
					j++;
					lst=inp[i]+md;
				}
			}
			if(j<n) r=md;
			else l=md;
		}
		printf("%.2lf\n",md);
	}
	return 0;
}