#include <iostream>
#include <vector>
#include <cmath>
#include <string>

using namespace std;

int solution(string dartResult)
{
    int answer=0,cnt=-1,i;
	vector<int> ret;
	for(i=0;i<dartResult.size();i++)
	{
		char tmp=dartResult[i];
		if(tmp>='0'&&tmp<='9')
		{
			cnt++;
			ret.push_back(tmp-'0');
		}
		if(tmp=='1'&&dartResult[i+1]=='0')
		{
			ret[cnt]=10;
			i++;
		}
		else if(tmp=='D')ret[cnt]*=ret[cnt];
		else if(tmp=='T')ret[cnt]=pow(ret[cnt],3);
		else if(tmp=='*')ret[cnt]*=2,ret[cnt-1]*=2;
		else if(tmp=='#')ret[cnt]*=-1;
	}
	for(i=0;i<3;i++)
		answer+=ret[i];
	return answer;
}