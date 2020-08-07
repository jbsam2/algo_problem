for t in range(int(input())):
    n=int(input());b=[list(map(int,input().split()))for _ in range(n)];a=[]
    for i in range(n):
        for j in range(n):
            if b[i][j]:
                w=h=0
                while b[i][j+w]:
                    w+=1
                    if w+j>=n:break
                while b[i+h][j]:
                    h+=1
                    if i+h>=n:break
                for k in range(h):
                    for l in range(w):b[i+k][j+l]=0
                a+=[[h,w]]
    print(f'#{t+1}',len(a),*sum(sorted(a,key=lambda x:(x[0]*x[1],x[0])),[]))