def convert_time(lst,tmp=[],start=[],end=[]):
	for i in lst:
		tmp.append(i.split())
		end_time=int(tmp[-1][1][0:2])*3600+int(tmp[-1][1][3:5])*60+int(tmp[-1][1][6:8])+float('0.'+tmp[-1][1][9:])
		end.append(end_time)
		start.append(round(end_time-float(tmp[-1][2][:-1])+0.001,3))
	return start,end
def solution(lines):
    answer = 0
    lst_start,lst_end=convert_time(lines)
    res=[]
    for k in lst_start+lst_end:
        cnt=0
        for i,j in zip(lst_start,lst_end):
            cnt+=1 if i<k+1 and j>=k else 0
        res.append(cnt)
    answer=max(res)
    return answer