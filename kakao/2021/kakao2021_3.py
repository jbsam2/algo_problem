# 시험 끝나고 시간초과 해결

from itertools import product as pro
d1=['python','java','cpp','-']
d2=['frontend','backend','-']
d3=['junior','senior','-']
d4=['pizza','chicken','-']
def solution(info,query):
    ret=[]
    d={''.join(i):[] for i in pro(d1,d2,d3,d4)}
    for i in info:
        t=i.split();t1=int(t[-1])
        for j in range(16):
            t2=t[:4]
            for k in range(4):
                if j&1<<k:t2[k]='-'
            d[''.join(t2)].append(t1)
    for q in query:
        cnt=0
        j=q.split(' and ')
        tmp=j[-1].split();j.pop();j+=[*tmp]
        score=int(j[-1])
        j=''.join(j[:4])
        for i in d[j]:
            if i>=score:cnt+=1
        ret.append(cnt)
    return ret