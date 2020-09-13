# 아직 오답

def totime(lst,start=[],end=[]):
    for i in lst:
        tmp=i.split('-')
        end+=[int(tmp[1][:2])*3600+int(tmp[1][3:5])*60+int(tmp[1][6:])]
        start+=[int(tmp[0][:2])*3600+int(tmp[0][3:5])*60+int(tmp[0][6:])]
    return start,end

def solution(play_time, adv_time, logs):
    if play_time<=adv_time: return '00:00:00'
    start,end=totime(logs);answer=0;maxtime=0
    adv=int(adv_time[:2])*3600+int(adv_time[3:5])*60+int(adv_time[6:])
    l=start+end
    for k in l[::-1]: # k부터 시작
        tmptime=0 
        for i,j in zip(start,end):
            if i <= (k+adv) and j>=k:
                tmptime+=(min(j,k+adv)-max(i,k))
        if tmptime > maxtime:
            maxtime = tmptime
            answer = k
    a='%02d:%02d:%02d'%(answer//3600,(answer%3600)//60,answer%60)
    return a