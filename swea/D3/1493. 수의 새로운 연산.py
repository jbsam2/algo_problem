b=[]
for i in range(1,300):
    for j in range(1,i+1):b.append((j,i-j+1))
for t in range(int(input())):
    p,q=map(int,input().split());res=b.index((b[p-1][0]+b[q-1][0],b[p-1][1]+b[q-1][1]))+1;print(f'#{t+1}',res)