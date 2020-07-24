#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

struct Treenode
{
	vector<Treenode *> childrun;
};

int n,y[100],x[100],r[100],longest;

int height(Treenode *root)
{
	vector<int> heights;
	for(int i=0;i<root->childrun.size();i++)
		heights.push_back(height(root->childrun[i]));
	if(heights.empty())return 0;
	sort(heights.begin(),heights.end());
	if(heights.size()>=2)
		longest=max(longest,2+heights[heights.size()-2]+heights[heights.size()-1]);
	return heights.back()+1;
}

int solve(Treenode *root)
{
	longest=0;
	int h=height(root);
	return max(longest,h);
}

int sqr(int x)
{
	return x*x;
}

int sqrdist(int a,int b)
{
	return sqr(y[a]-y[b])+sqr(x[a]-x[b]);
}

bool encloses(int a,int b)
{
	return r[a]>r[b] && sqrdist(a,b)<sqr(r[a]-r[b]);
}

bool ischild(int parent,int child)
{
	if(!encloses(parent,child))
		return false;
	for(int i=0;i<n;i++)
		if(i!=parent && i!=child && encloses(parent,i) && encloses(i,child))
			return false;
	return true;
}

Treenode *getTree(int root)
{
	Treenode *ret=new Treenode();
	for(int ch=0;ch<n;ch++)
		if(ischild(root,ch))
			ret->childrun.push_back(getTree(ch));
	return ret;
}

int main()
{
	int t;
	cin>>t;
	while(t--)
	{
		cin>>n;
		for(int i=0;i<n;i++)
			cin>>x[i]>>y[i]>>r[i];
		Treenode *T=getTree(0);
		cout<<solve(T)<<endl;
	}
	return 0;
}