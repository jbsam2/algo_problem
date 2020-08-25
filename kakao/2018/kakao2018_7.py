def totime(lst,start=[],end=[]):
    for i in lst:
        tmp = i.split()
        end.append(int(tmp[1][0:2])*3600+int(tmp[1][3:5])*60+int(tmp[1][6:8])+float('0.'+tmp[1][9:]))
        start.append(round(end[-1]-float(tmp[2][:-1])+0.001,3))
    return start,end
def solution(lines):
    lst_start,lst_end=totime(lines);res=[]
    for k in lst_start+lst_end:
        cnt=0
        for i,j in zip(lst_start,lst_end):
            if i<k+1 and j>=k : cnt+=1
        res.append(cnt)
    return max(res)