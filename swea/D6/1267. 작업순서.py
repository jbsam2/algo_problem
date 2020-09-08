for t in range(10):
    v,e=map(int,input().split());l=[*map(int,input().split())];b=[[]for _ in range(v+1)];ret=[]
    for i in range(e):s=l[2*i];f=l[2*i+1];b[f].append(s)    
    while 1:
        if len(ret)==v:break
        s=[]
        for i in range(1,v+1):
            if not b[i] and i not in ret:s.append(i)
        for i in s:
            ret.append(i)
            for j in range(v+1):
                if i in b[j]:b[j].remove(i)
    print(f'#{t+1}',*ret)


for t in range(10):
    v,e=map(int,input().split());l=[*map(int,input().split())];b=[[]for _ in range(v+1)];ret=set()
    for i in range(e):s=l[2*i];f=l[2*i+1];b[f].append(s)    
    while 1:
        if len(ret)==v:break
        s=[]
        for i in range(1,v+1):
            if not b[i]:s.append(i)
        for i in s:
            ret.add(i)
            for j in range(v+1):
                if i in b[j]:b[j].remove(i)
    print(f'#{t+1}',*ret)