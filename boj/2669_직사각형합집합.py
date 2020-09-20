b=[[0]*101 for _ in range(101)]
for _ in range(4):
    l=[*map(int,input().split())]
    for i in range(l[1],l[3]):
        for j in range(l[0],l[2]):b[i][j]=1
print(sum(sum(b,[])))