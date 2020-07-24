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

int main()
{
	int n,i,size,x,y;
	vector<vector2> hull1,hull2;
	cin>>n;
	while(n--)
	{
		cin>>x>>y;
		hull1.push_back(vector2(x,y));
	}
	for(i=1;i<hull1.size();i++)
		if(hull1[i]<hull1[0])
			swap(hull1[0],hull1[i]);
	piv=hull1[0];
	sort(hull1.begin()+1,hull1.end(),cmp);
	hull1.push_back(piv);

	hull2.push_back(hull1[0]);
	hull2.push_back(hull1[1]);

	for(i=2;i<hull1.size();i++)
	{
		while(hull2.size()>1&&ccw(hull2[hull2.size()-2],hull2[hull2.size()-1],hull1[i])<=0)
			hull2.pop_back();
		hull2.push_back(hull1[i]);
	}
	cout<<hull2.size()-1<<endl;
	for(i=0;i<hull2.size()-1;i++)
		cout<<hull2[i].x<<" "<<hull2[i].y<<endl;
	return 0;
}