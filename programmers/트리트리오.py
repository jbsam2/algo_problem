from collections import deque
dst=[]
a=[[] for _ in range(250001)]
def bfs(st,n):
    global dst
    q=deque([(st,0)]);v=[1]*(n+1);ret=(st,0);v[st]=0
    while q:
        tmp=q.popleft();l=tmp[1];p=tmp[0]
        if l>ret[1]:ret=tmp;dst=[p]
        elif l==ret[1]:dst.append(p)
        for i in a[p]:
            if v[i]:v[i]=0;q.append((i,l+1))
    return ret

def solution(n, edges):
    for i in edges:a[i[0]].append(i[1]);a[i[1]].append(i[0])
    x = bfs(1,n);y = bfs(x[0],n)
    if len(dst)>1:return y[1]
    z = bfs(y[0],n)
    if len(dst)>1:return y[1]
    elif len(dst)==1:return y[1]-1
    return -1