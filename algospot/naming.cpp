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

vector<int> getprefixsuffix(const string& s)
{
	vector<int> ret,pi=getpartialmatch(s);
	int k=s.size();
	while(k>0)
	{
		ret.push_back(k);
		k=pi[k-1];
	}
	return ret;
}

int main()
{
	string dad,mom;
	cin>>dad>>mom;
	string combined=dad+mom;
	vector<int> ret=getprefixsuffix(combined);
	for(int i=ret.size()-1;i>=0;i--)
		cout<<ret[i]<<" ";
	return 0;
}

#include <iostream> 
#include <cstring>
#include <cmath>
#include <cstdio>
using namespace std; 
 
char s1[400001];
int table[400001];
int result[400001];
int main()
{
    gets(s1);
    gets(s1+strlen(s1));
 
    int begin=1,matched=0,len=strlen(s1);
    while(begin+matched<len)
    {
        if(s1[matched]==s1[begin+matched])
        {
            matched++;
            table[begin+matched-1]=matched;
        }
        else
        {
            if(matched == 0)
            	begin++;
            else
            {
                begin+=matched-table[matched];
                matched=table[matched];
            }
        }
    }
    int ridx=1;
    result[0]=len;
    while(table[len-1]!=0)
    {
        result[ridx++]=table[len-1];
        len=table[len-1];
    }
 
    for(int i=ridx-1;i>=0;i--)
    {
        printf("%d%c",result[i],i?' ':'\n');
    }
    return 0;
}