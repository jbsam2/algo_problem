#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int gcd(int a,int b)
{
	return b?gcd(b,a%b):a;
}

int ceil(int a,int b)
{
	return (a+b-1)/b;
}

vector<int> solve(const vector<int>& recipe,const vector<int>& put)
{
	int n=recipe.size();
	int b=recipe[0];
	for(int i=1;i<n;i++)
		b=gcd(b,recipe[i]);
	int a=b;
	for(int i=0;i<n;i++)
		a=max(a,ceil(put[i]*b,recipe[i]));
	vector<int> ret(n);
	for(int i=0;i<n;i++)
		ret[i]=recipe[i]*a/b-put[i];
	return ret;
}

int main()
{
	int t,num,tmp;
	cin>>t;
	while(t--)
	{
		vector<int> recipe,put;
		cin>>num;
		for(int i=0;i<num;i++)
		{
			cin>>tmp;
			recipe.push_back(tmp);
		}
		for(int i=0;i<num;i++)
		{
			cin>>tmp;
			put.push_back(tmp);
		}
		vector<int> ret=solve(recipe,put);
		for(int i=0;i<ret.size();i++)
			cout<<ret[i]<<" ";
		cout<<endl<<endl;
	}
	return 0;
}

#include<ios>
int n,t,i,a[1001][2],l,g;int G(int a,int b){return b?G(b,a%b):a;}int main(){scanf("%d",&t);while(t--){scanf("%d",&n);for(i=0;i<n;i++)scanf("%d",&a[i][0]);g=a[i][0],l=0;for(i=1;i<n;i++)g=G(g,a[i][0]);for(i=0;i<n;i++)a[i][0]/=g;for(i=0;i<n;i++){scanf("%d",&a[i][1]);if(l<(a[i][1]-1)/a[i][0]+1)l=(a[i][1]-1)/a[i][0]+1;}for(i=0;i<n;i++)printf("%d ",a[i][0]*l-a[i][1]);printf("\n");}}