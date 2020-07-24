#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

vector<int> slice(const vector<int>& v,int a,int b)
{
	return vector<int>(v.begin()+a,v.begin()+b);
}

void printpostorder(const vector<int>& preorder,const vector<int>& inorder)
{
	const int n=preorder.size();
	if(preorder.empty()) return;

	const int root=preorder[0];
	const int l=find(inorder.begin(),inorder.end(),root)-inorder.begin();
	const int r=n-1-l;
	printpostorder(slice(preorder,1,l+1),slice(inorder,0,l));
	printpostorder(slice(preorder,l+1,n),slice(inorder,l+1,n));
	cout<<root<<' ';
}
int main()
{
	int t,n,tmp,i;
	cin>>t;
	while(t--)
	{
		cin>>n;
		vector<int> preorder,inorder;
		for(i=0;i<n;i++)
		{
			cin>>tmp;
			preorder.push_back(tmp);
		}
		for(i=0;i<n;i++)
		{
			cin>>tmp;
			inorder.push_back(tmp);
		}
		printpostorder(preorder,inorder);
		cout<<endl;
	}
	return 0;
}