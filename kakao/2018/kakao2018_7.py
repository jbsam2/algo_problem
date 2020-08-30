def totime(lst,start=[],end=[]):
    for i in lst:
        tmp=i.split()
        end+=[int(tmp[1][0:2])*3600+int(tmp[1][3:5])*60+int(tmp[1][6:8])+float('0.'+tmp[1][9:])]
        start+=[round(end[-1]-float(tmp[2][:-1])+0.001,3)]
    return start,end
def solution(lines):
    start,end=totime(lines);res=[]
    for k in start+end:
        cnt=0
        for i,j in zip(start,end):
            if i<k+1 and j>=k:cnt+=1
        res+=[cnt]
    return max(res)