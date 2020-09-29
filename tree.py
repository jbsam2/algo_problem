from copy import deepcopy
def solution(n, edges):
    answer=[]
    for i in range(n-1):
        for j in range(i,n-1):
            b=[[]for _ in range(n)]
            tmpedge=deepcopy(edges)
            tmpedge.pop(i)
            tmpedge.pop(j-1)
            for k in tmpedge:
                b[k[0]].append(k[1])
                b[k[1]].append(k[0])
            s1=s2=s3=0
            v=[];q=[]
            for k in range(n):
                if k not in v:
                    q=[k];break
            while q:
                qq=q.pop()
                v.append(qq)
                for k in b[qq]:
                    if k not in v:q.append(k)
            s1=len(v)
            q=[]
            for k in range(n):
                if k not in v:
                    q=[k];break
            while q:
                qq=q.pop()
                v.append(qq)
                for k in b[qq]:
                    if k not in v:q.append(k)
            s2=len(v)-s1
            q=[]
            for k in range(n):
                if k not in v:
                    q=[k];break
            while q:
                qq=q.pop()
                v.append(qq)
                for k in b[qq]:
                    if k not in v:q.append(k)
            s3=n-s2-s1
            if s1==s2==s3:answer=[i,j]
    return answer

print(solution(9,[[0,2],[2,1],[2,4],[3,5],[5,4],[5,7],[7,6],[6,8]]))