#include <string>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
using namespace std;

double str2time(bool flag,string time)
{
	double ret=0,msec=0;
	int sec=0;
	if(flag)
	{
		int hour=((time[0]-'0')*10+(time[1]-'0'))*3600;
		int minite=((time[3]-'0')*10+(time[4]-'0'))*60;
		sec=(time[6]-'0')*10+(time[7]-'0');
		msec=((time[9]-'0')/10.0)+((time[10]-'0')/100.0)+((time[11]-'0')/1000.0);
		ret=(double)(hour+minite+sec)+msec;
	}
	else
	{
		for(int i=0;i<time.size()-1;i++)
		{
			if(i==0)sec=(time[0]-'0');
			else if(i>1)msec+=(time[i]-'0')/pow(10,i-1);
		}
		ret=(double)sec+msec-0.001;
	}
	return ret;
}

int solution(vector<string> lines)
{
	vector<double> stlog,endlog,log;
	int answer=0;
	for(int i=0;i<lines.size();i++)
		stlog.push_back(str2time(true,lines[i].substr(11,12))-str2time(false,lines[i].substr(24)));
	for(int i=0;i<lines.size();i++)
		endlog.push_back(str2time(true,lines[i].substr(11,12)));
	for(int i=0;i<lines.size()*2;i++)
	{
		if(i%2==0)log.push_back(str2time(true,lines[i/2].substr(11,12))-str2time(false,lines[i/2].substr(24)));
		else log.push_back(str2time(true,lines[i/2].substr(11,12)));
	}
	for(int i=0;i<log.size();i++)
	{
		int tmp=0;
		for(int j=0;j<stlog.size();j++)
		{
			if((stlog[j]<log[i]+1)&&(endlog[j]>=log[i]))tmp++;
		}
		if(tmp>answer)answer=tmp;
	}
	return answer;
}