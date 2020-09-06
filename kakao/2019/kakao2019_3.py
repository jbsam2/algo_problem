def possi(vec,now):
    for i in vec:
        if i&now==i:return 0
    return 1

def solution(relation):
    n=len(relation);m=len(relation[0]);answer=[]
    for i in range(1<<m):
        s=set()
        for j in range(n):
            now=''
            for k in range(m):
                if i&(1<<k): now+=relation[j][k]
            s.add(now)
        if len(s)==n and possi(answer,i):answer.append(i)
    return len(answer)