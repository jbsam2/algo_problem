for t in range(int(input())):
    v,e,a,b=map(int,input().split());l=[*map(int,input().split())];tr=[0]*(v+1)
    for i in range(e):tr[l[2*i+1]]=l[2*i]
    t1=[];t2=[];s=[0]*(v+1)
    for i in range(1,v+1):
        j=i
        while j:
            if i==a:t1.append(j)
            if i==b:t2.append(j)
            s[j]+=1;j=tr[j]
    for i in t1:
        if i in t2:print(f'#{t+1}',i,s[i]);break