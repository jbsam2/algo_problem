for t in range(int(input())):
    n=int(input());b=[list(map(int,input().split())) for _ in range(n)];a=[]
    for i in range(n):
        for j in range(n):
            if b[i][j]:
                w=1;d=j
                while 1:
                    d+=1
                    if d>=n:break
                    if b[i][d]:w+=1
                    else:break
                h=1;d=i
                while 1:
                    d+=1
                    if d>=n:break
                    if b[d][j]:h+=1
                    else:break
                for k in range(i,i+h):
                    for l in range(j,j+w):
                        b[k][l]=0
                a.append([h,w,h*w])
    a=sorted(a,key=lambda x:(x[2],x[0]))
    print(f'#{t+1}',len(a),end=' ')
    for r,c,_ in a:print(r,c,end=' ')
    print()