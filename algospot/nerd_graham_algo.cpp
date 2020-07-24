#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

const double pi=4.0*acos(0.0);

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

double ccw(vector2 p,vector2 a,vector2 b)
{
	return (a-p).cross(b-p);
}

vector2 piv;

bool cmp(vector2 a,vector2 b)
{
   return (a-piv).cross(b-piv)>0;
};

bool segmentintersects(vector2 a,vector2 b,vector2 c,vector2 d)
{
	double ab=ccw(a,b,c)*ccw(a,b,d);
	double cd=ccw(c,d,a)*ccw(c,d,b);
	if(ab==0&&cd==0)
	{
		if(b<a)swap(a,b);
		if(d<c)swap(c,d);
		return !(b<c||d<a);
	}
	return ab<=0&&cd<=0;
}

bool isinside(vector2 q,const vector<vector2>& p)
{
	int cross=0;
	for(int i=0;i<p.size();i++)
	{
		int j=(i+1)%p.size();
		if((p[i].y>q.y)!=(p[j].y>q.y))
		{
			double atx=(p[j].x-p[i].x)*(q.y-p[i].y)/(p[j].y-p[i].y)+p[i].x;
			if(q.x<atx)cross++;
		}
	}
	return cross%2>0;
}

typedef vector<vector2> polygon;

polygon giftwrap(vector<vector2>& p)
{
    int i,n=p.size();
    vector<vector2> hull;

    for(i=1;i<n;++i)
        if(p[i]<p[0])
            swap(p[0],p[i]);
    piv=p[0];
    sort(p.begin()+1,p.end(),cmp);
    p.push_back(p[0]);

    hull.push_back(p[0]);
    hull.push_back(p[1]);

    for(i=2;i<n;++i)
    {
        while(hull.size()>1 && ccw(hull[hull.size()-2],hull[hull.size()-1],p[i])<=0)
        	hull.pop_back();

        hull.push_back(p[i]);
    }
    return hull;
}

bool polygonintersects(const polygon& p,const polygon& q)
{
	int n=p.size(),m=q.size();
	if(isinside(p[0],q)||isinside(q[0],p))return true;
	for(int i=0;i<n;i++)
		for(int j=0;j<m;j++)
			if(segmentintersects(p[i],p[(i+1)%n],q[j],q[(j+1)%m]))return true;
	return false;
}

int main()
{
	int t,cand,x,y;
	cin>>t;
	while(t--)
	{
		cin>>cand;
		polygon nerd,notnerd;
		while(cand--)
		{
			bool isnerd;
			cin>>isnerd>>x>>y;
			if(isnerd)nerd.push_back(vector2(x,y));
			else notnerd.push_back(vector2(x,y));
		}
		polygon nerdhull=giftwrap(nerd);
		polygon notnerdhull=giftwrap(notnerd);
		if(polygonintersects(nerdhull,notnerdhull))
			cout<<"THEORY IS INVALID"<<endl;
		else cout<<"THEORY HOLDS"<<endl;
	}
	return 0;
}