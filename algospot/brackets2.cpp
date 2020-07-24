#include <iostream>
#include <string>
#include <stack>
using namespace std;

bool wellmatch(const string& formula)
{
	const string opening("({["),closing(")}]");
	stack<char> openstack;
	for(int i=0;i<formula.size();i++)
	{
		if(opening.find(formula[i])!=-1)
			openstack.push(formula[i]);
		else
		{
			if(openstack.empty())return false;
			if(opening.find(openstack.top())!=closing.find(formula[i]))return false;
			openstack.pop();
		}
	}
	return openstack.empty();
}

int main()
{
	int t;
	cin>>t;
	while(t--)
	{
		string s;
		cin>>s;
		if(wellmatch(s))
			cout<<"YES"<<endl;
		else
			cout<<"NO"<<endl;
	}
	return 0;
}