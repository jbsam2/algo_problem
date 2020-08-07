for t in range(10):
    d=int(input());b=sorted(map(int,input().split()))
    for _ in range(d):b[0]+=1;b[-1]-=1;b.sort()
    print(f'#{t+1}',b[-1]-b[0])