#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
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

int maxoverlap(const string& a,const string& b)
{
	int n=a.size(),m=b.size();
	vector<int> pi=getpartialmatch(b);
	int begin=0,matched=0;
	while(begin<n)
	{
		if(matched<m&&a[begin+matched]==b[matched])
		{
			matched++;
			if(begin+matched==n)
				return matched;
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
	return 0;
}

int main()
{
	int t;
	cin>>t;
	while(t--)
	{
		string o,r;
		cin>>o;
		for(int i=o.size()-1;i>=0;i--)
			r+=o[i];
		int ret=2*o.length()-maxoverlap(o,r);
		cout<<ret<<endl;
	}
	return 0;
}

#include <iostream>
#include <cstring>
using namespace std;

char input[100001];
char input_reverse[100001];
int partMatch[100001];

int main(void)
{
    int C;
    ios_base::sync_with_stdio(false);
	cin.tie(NULL);
    cin >> C;
    while(C--)
    {
        cin>>input;
        int input_len = strlen(input);
        for(int i=input_len-1;i>=0;i--)
            input_reverse[input_len-i-1]=input[i];
        input_reverse[input_len]='\0';
        if(strcmp(input,input_reverse)==0)
        {
            cout<<input_len<<'\n';
            continue;
        }
        int begin=1,matched=0;
        while(begin+matched<input_len)
        {
            if(input[begin+matched]==input_reverse[matched])
            {
                matched++;
                partMatch[begin+matched-1]=matched;
            }
            else
            {
                if(matched == 0)
                    begin++;
                else
                {
                    begin+=matched-partMatch[matched-1];
                    matched=partMatch[matched-1];
                }
            }
        }
        cout<<(input_len*2)-partMatch[input_len-1]<<'\n';
    }
    return 0;
}