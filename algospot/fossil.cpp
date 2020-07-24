#include <iostream>
#include <algorithm>
#include <vector>
#include <iomanip>
using namespace std;

typedef struct
{
	double y,x;
}point;

vector<point> hull1,hull2;
vector<pair<point,point>>upper,lower;

void decompose(const vector<point>& hull)
{
	int n=hull.size();
	for(int i=0;i<n;i++)
	{
		if(hull[i].x<hull[(i+1)%n].x)
			lower.push_back(make_pair(hull[i],hull[(i+1)%n]));
		else if(hull[i].x>hull[(i+1)%n].x)
			upper.push_back(make_pair(hull[i],hull[(i+1)%n]));
	}
}

bool between(const point& a,const point& b,double x)
{
	return (a.x<=x&&x<=b.x)||(b.x<=x&&x<=a.x);
}

double at(const point& a,const point& b,double x)
{
	double dy=b.y-a.y,dx=b.x-a.x;
	return a.y+dy*(x-a.x)/dx;
}

double vertical(double x)
{
	double minup=1e20, maxlow=-1e20;
	for(int i=0;i<upper.size();i++)
		if(between(upper[i].first,upper[i].second,x))
			minup=min(minup,at(upper[i].first,upper[i].second,x));
	for(int i=0;i<lower.size();i++)
		if(between(lower[i].first,lower[i].second,x))
			maxlow=max(maxlow,at(lower[i].fist,lower[i].second,x));
	return minup-maxlow;
}

double minx(vector<point> &p)
{
	double ret=p[0].x;
	for(int i=1;i<p.size();i++)
		ret=min(ret,p[i].x);
	return ret;
}
double maxx(vector<point> &p)
{
	double ret=p[0].x;
	for(int i=1;i<p.size();i++)
		ret=max(ret,p[i].x);
	return ret;
}

double solve()
{
	double lo=max(minx(hull1),minx(hull2));
	double hi=min(maxx(hull1),maxx(hull2));
	if(hi<lo)return 0;

	for(int i=0;i<100;i++)
	{
		double aab=(2*lo+hi)/3.0,abb=(lo+2*hi)/3.0;
		if(vertical(aab)<vertical(abb))lo=aab;
		else hi=abb;
	}
	return max(0.0,vertical(hi));
}

int main()
{
	int t,n1,n2;
	point tmp;
	cin>>t;
	while(t--)
	{
		cin>>n1>>n2;
		hull1.clear();
		hull2.clear();
		for(int i=0;i<n1;i++)
		{
			cin>>tmp.x>>tmp.y;
			hull1.push_back(tmp);
		}
		for(int i=0;i<n2;i++)
		{
			cin>>tmp.x>>tmp.y;
			hull2.push_back(tmp);
		}
		lower.clear();
		upper.clear();
		decompose(hull1);
		decompose(hull2);
		double ret=solve();
		if(ret<=0)cout<<"0.000000"<<endl;
		else
		{
			cout<<fixed<<setprecision(10);
			cout<<ret<<endl<<endl;
		}
	}
	return 0;
}