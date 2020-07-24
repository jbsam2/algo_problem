#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int str2time(string time)
{
	return((time[0]-'0')*10+(time[1]-'0'))*60+(time[3]-'0')*10+(time[4]-'0');
}

string solution(int n,int t,int m,vector<string> timetable)
{
	string answer="";
	int ans,num;
	num=timetable.size();
	vector<int> timearr;
	
	for(int i=0;i<num;i++)
		timearr.push_back(str2time(timetable[i]));

	sort(timearr.begin(),timearr.end());

	int drivetime=540,people=0;

	for(int i=0;i<n;i++)
	{
		int seat=m;
		for(int j=people;j<num;j++)
		{
			if(timearr[j]<=drivetime)
			{
				seat--;
				people++;
				if(seat==0)break;
			}
		}
		if(i==n-1)
		{
			if(seat==0)ans=timearr[people-1]-1;
			else ans=drivetime;
		}
		drivetime+=t;
		if(drivetime>=1440)break;
	}
	if((ans/60)<10)answer+="0";
	answer+=to_string(ans/60);
	ans%=60;
	answer+=":";
	if(ans<10)answer+="0";
	answer+=to_string(ans);
	return answer;
}