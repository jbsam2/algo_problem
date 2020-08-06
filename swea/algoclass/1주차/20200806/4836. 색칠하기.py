for t in range(int(input())):
    n=int(input());r=[];b=[];a=[]
    for i in range(n):
        y1,x1,y2,x2,c=map(int,input().split())
        for y in range(y1,y2+1):
            for x in range(x1,x2+1):
                if c==1:r.append((y,x))
                elif c==2:b.append((y,x))    
    for i in b:
        if i in r:a.append(i)
    print(f'#{t+1}',len(a))