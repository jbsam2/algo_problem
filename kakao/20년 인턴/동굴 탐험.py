def solution(n, path, order):
    b=[[] for i in range(n)]
    while path:s,e=path.pop();b[s].append(e);b[e].append(s)
    dest=set();s2e=[0]*n
    for s,e in order:dest.add(e);s2e[s]=e
    q=[0];v=[0]*n
    while q:
        node=q.pop();v[node]=1;e=s2e[node]
        if e:
            dest.remove(e)
            if v[e]:q.extend([i for i in b[e] if v[i]==0])
        elif node in dest:continue
        q.extend([i for i in b[node] if v[i]==0])
    return not dest