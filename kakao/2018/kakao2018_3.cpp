#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int solution(int cacheSize,vector<string> cities)
{
	vector<string> q;
	int answer=0;
	for(vector<string>::iterator i=cities.begin();i!=cities.end();i++)
	{
		transform(i->begin(),i->end(),i->begin(),::tolower);
		bool flag=false;
		for(vector<string>::iterator j=q.begin();j!=q.end();j++)
		{
			if(*j==*i)
			{
				flag=true;
				answer+=1;
				q.erase(j);
				q.push_back(*i);
				break;
			}
		}
		if(!flag)
		{
			answer+=5;
			if(cacheSize!=0&&q.size()==cacheSize)
				q.erase(q.begin());
			if(q.size()<cacheSize)
				q.push_back(*i);
		}
	}
	return answer;
}