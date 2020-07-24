#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>
#include <cassert>
using namespace std;

const double pi=4.0*acos(0.0);
const double EPSILON=1e-9;
const double INF=1e200;

struct vector2
{
	double x,y;
	explicit vector2(double x_=0,double y_=0):x(x_),y(y_)
	{}
	//벡터 비교
	bool operator==(const vector2& rhs)const
	{
		return x==rhs.x&&y==rhs.y;
	}
	bool operator<(const vector2& rhs)const
	{
		return x!=rhs.x?x<rhs.x:y<rhs.y;
	}
	//벡터 연산
	vector2 operator+(const vector2& rhs)const
	{
		return vector2(x+rhs.x,y+rhs.y);
	}
	vector2 operator-(const vector2& rhs)const
	{
		return vector2(x-rhs.x,y-rhs.y);
	}
	vector2 operator*(double rhs)const
	{
		return vector2(x*rhs,y*rhs);
	}
	//벡터 길이
	double norm()const
	{
		return hypot(x,y);
	}
	//단위벡터
	vector2 normalize()const
	{
		return vector2(x/norm(),y/norm());
	}
	//x축에서 부터 각도
	double polar()const
	{
		return fmod(atan2(y,x)+pi,pi);
	}
	//내적, 외적
	double dot(const vector2& rhs)const
	{
		return x*rhs.x+y*rhs.y;
	}
	double cross(const vector2& rhs)const
	{
		return x*rhs.y-y*rhs.x;
	}
	//벡터가 rhs에 그림자 내릴때
	vector2 project(const vector2& rhs)const
	{
		vector2 r=rhs.normalize();
		return r*r.dot(*this);
	}
};

double ccw1(vector2 a,vector2 b)
{
	return a.cross(b);
}

double ccw2(vector2 p,vector2 a,vector2 b)
{
	return ccw1(a-p,b-p);
}

bool lineintersection(vector2 a,vector2 b,vector2 c,vector2 d,vector2 &x)
{
	double det=(b-a).cross(d-c);
	if(fabs(det)<EPSILON)
		return false;
	x=a+(b-a)*((c-a).cross(d-c)/det);
	return true;
}

double area(const vector<vector2>& p)
{
	double ret=0;
	for(int i=0;i<p.size();i++)
	{
		int j=(i+1)%p.size();
		ret+=p[i].x*p[j].y-p[i].y*p[j].x;
	}
	return fabs(ret)/2.0;
}

typedef vector<vector2> polygon;

polygon cutpoly(const polygon& p,const vector2& a,const vector2& b)
{
	int n=p.size();
	vector<bool> inside(n);
	for(int i=0;i<n;i++)
		inside[i]=ccw2(a,b,p[i])>=0;
	polygon ret;
	for(int i=0;i<n;i++)
	{
		int j=(i+1)%n;
		if(inside[i])ret.push_back(p[i]);
		if(inside[i]!=inside[j])
		{
			vector2 cross;
			assert(lineintersection(p[i],p[j],a,b,cross));
			ret.push_back(cross);
		}
	}
	return ret;
}

polygon intersection(const polygon& p,double x1,double y1,double x2,double y2)
{
	vector2 a(x1,y1),b(x2,y1),c(x2,y2),d(x1,y2);
	polygon ret=cutpoly(p,a,b);
	ret=cutpoly(ret,b,c);
	ret=cutpoly(ret,c,d);
	ret=cutpoly(ret,d,a);
	return ret;
}

int main()
{
	int t,x1,x2,y1,y2,n;
	cin>>t;
	while(t--)
	{
		cin>>x1>>y1>>x2>>y2>>n;
		polygon island(n);
		for(int i=0;i<n;i++)
			cin>>island[i].x>>island[i].y;
		cout<<fixed<<setprecision(10);
		cout<<area(intersection(island,x1,y1,x2,y2))<<endl<<endl;
	}
	return 0;
}