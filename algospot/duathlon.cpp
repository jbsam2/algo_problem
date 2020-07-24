#include <iostream>
#include <algorithm>
#include <vector>
#include <iomanip>
using namespace std;

double t,run;
vector<double> runspeed,cyclespeed;

double time(int i,double r)
{
	double c=t-r;
	return r/runspeed[i]+c/cyclespeed[i];
}

double diff(double r)
{
	int n=runspeed.size();
	double cheater=time(n-1,r);
	double other=time(0,r);
	for(int i=1;i<n-1;i++)
		other=min(other,time(i,r));
	return other-cheater;
}

double maxdiff()
{
	double lo=0,hi=t,ret;
	for(int i=0;i<100;i++)
	{
		double aab=(2*lo+hi)/3,abb=(lo+2*hi)/3;
		if(diff(aab)>diff(abb))	hi=abb;
		else lo=aab;
	}
	ret=(lo+hi)/2;
	if(diff(ret)>0) return ret;
	else return -1;
}

int main()
{
	int test,n;
	double rtmp,ctmp;
	cin>>test;
	while(test--)
	{
		cin>>t;
		cin>>n;
		for(int i=0;i<n;i++)
		{
			cin>>rtmp>>ctmp;
			runspeed.push_back(rtmp);
			cyclespeed.push_back(ctmp);
		}
		cout<<fixed<<setprecision(2);
		if(maxdiff()>0)
			cout<<maxdiff()<<" "<<t-maxdiff()<<endl<<endl;
		else
			cout<<"impossible"<<endl<<endl;
	}
	return 0;
}