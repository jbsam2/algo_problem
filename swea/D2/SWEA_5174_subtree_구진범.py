def sol(n):
    global cnt,v
    cnt+=1;v+=[n]
    for i in l[n]:
        if i not in v:sol(i)
for t in range(int(input())):
    e,n=map(int,input().split());l=[[]for _ in range(e+2)];cnt=0;v=[];tmp=[*map(int,input().split())]
    for i in range(e):l[tmp[2*i]].append(tmp[2*i+1])
    sol(n);print('#{}'.format(t+1),cnt)