#include <iostream>
#include <string>
#include <cmath>
using namespace std;

int composition,wordnum,sentencenum;
int classified[100];
double be[501];
double rightafter[501][501];
double missmatch[501][501];
int choice[102][502];
double cache[102][502];
string word[501];

double recognize(int segment,int previousmatch)
{
	if(segment==composition)
		return 0;
	double &ret=cache[segment][previousmatch];
	if(ret!=1.0)
		return ret;
	ret=-1e200;
	int &choose=choice[segment][previousmatch];
	for(int thismatch=1;thismatch<=wordnum;thismatch++)
	{
		double candidate=rightafter[previousmatch][thismatch]+missmatch[thismatch][classified[segment]]+recognize(segment+1,thismatch);
		if(ret<candidate)
		{
			ret=candidate;
			choose=thismatch;
		}
	}
	return ret;
}

string reconstruct(int segment,int previousmatch)
{
	int choose=choice[segment][previousmatch];
	string ret=word[choose];
	if(segment<composition-1)
		ret=ret+" "+reconstruct(segment+1,choose);
	return ret;
}

void initialize()
{
	for(int i=0;i<composition;i++)
		for(int j=0;j<=wordnum;j++)
			cache[i][j]=1.0;
}
int main()
{
	cin>>wordnum>>sentencenum;
	for(int i=1;i<=wordnum;i++)
		cin>>word[i];
	for(int i=1;i<=wordnum;i++)
	{
		cin>>be[i];
		be[i]=log(be[i]);
	}
	for(int i=0;i<=wordnum;i++)
		for(int j=1;j<=wordnum;j++)
		{
			if(i==0)
				rightafter[i][j]=be[j];
			else
			{
				cin>>rightafter[i][j];
				rightafter[i][j]=log(rightafter[i][j]);
			}
		}
	for(int i=1;i<=wordnum;i++)
		for(int j=1;j<=wordnum;j++)
		{
			cin>>missmatch[i][j];
			missmatch[i][j]=log(missmatch[i][j]);
		}
	while(sentencenum--)
	{
		cin>>composition;

		initialize();
		for(int i=0;i<composition;i++)
		{
			string input;
			cin>>input;
			for(int j=1;j<=wordnum;j++)
				if(input==word[j])
				{
					classified[i]=j;
					break;
				}
		}
		recognize(0,0);
		cout<<reconstruct(0,0)<<endl;
	}
	return 0;
}