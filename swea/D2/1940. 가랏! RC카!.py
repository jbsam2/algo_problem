for t in range(int(input())):
    v=d=0
    for i in range(int(input())):
        c=list(map(int,input().split()))
        if c[0]==1:v+=c[1]
        elif c[0]==2:
            v-=c[1]
            if v<=0:v=0
        d+=v      
    print(f'#{t+1}',d)