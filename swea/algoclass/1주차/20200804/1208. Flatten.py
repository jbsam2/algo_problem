for t in range(10):
    n=int(input());b=list(map(int,input().split()));r=0
    for i in range(n):
        if max(b)-min(b)<=1:break
        b[b.index(max(b))]-=1;b[b.index(min(b))]+=1
    print(f'#{t+1}',max(b)-min(b))