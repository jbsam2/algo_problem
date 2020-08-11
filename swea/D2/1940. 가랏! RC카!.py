for t in range(int(input())):
    c=int(input());v=d=0
    for a in range(c):
        l=list(map(int, input().split()))
        if l[0]==1:v+=l[1]
        elif l[0]==2:
            v-=l[1]
            if v<=0:v=0
        d+=v      
    print(f'#{t+1}',d)