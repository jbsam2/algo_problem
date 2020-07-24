#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<int> getpartialmatch(const string& n)
{
	int m=n.size();
	vector<int> pi(m,0);
	int begin=1,matched=0;
	while(begin+matched<m)
	{
		if(n[begin+matched]==n[matched])
		{
			matched++;
			pi[begin+matched-1]=matched;
		}
		else
		{
			if(matched==0)
				begin++;
			else
			{
				begin+=matched-pi[matched-1];
				matched=pi[matched-1];
			}
		}
	}
	return pi;
}

int kmp(const string& H,const string& N)
{
	int n=H.size(),m=N.size();
	vector<int> pi=getpartialmatch(N);
	int begin=0,matched=0;
	while(begin<=n-m)
	{
		if(matched<m&&H[begin+matched]==N[matched])
		{
			matched++;
			if(matched==m)return begin;
		}
		else
		{
			if(matched==0)begin++;
			else
			{
				begin+=matched-pi[matched-1];
				matched=pi[matched-1];
			}
		}
	}
	return 0;
}

int main()
{
	int t,i,n;
	cin>>t;
	while(t--)
	{
		cin>>n;
		vector<string> dial;
		for(i=0;i<=n;i++)
		{
			string tmp;
			cin>>tmp;
			dial.push_back(tmp);
		}
		int ret=0;
		for(i=0;i<n;i++)
		{
			int clock=i%2;
			if(clock)ret+=kmp(dial[i]+dial[i],dial[i+1]);
			else ret+=kmp(dial[i+1]+dial[i+1],dial[i]);
		}
		cout<<ret<<endl;
	}
	return 0;
}