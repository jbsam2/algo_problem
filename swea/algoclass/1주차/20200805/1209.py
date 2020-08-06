for t in range(10):
    n=int(input());b=[];ans= t2=t3=0
    for i in range(100):b.append(list(map(int,input().split())));ans=max(ans,sum(b[i]))
    for i in range(100):
        t1=[];t2+=b[i][i];t3+=b[i][99-i]
        for j in range(100):t1.append(b[j][i])
        ans=max(ans,sum(t1))
    ans=max(ans,t2,t3)
    print(f'#{t+1}',ans)