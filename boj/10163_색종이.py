b=[[0]*101 for _ in range(101)];n=1
for _ in range(int(input())):
    l=[*map(int,input().split())]
    for i in range(l[1],l[1]+l[3]):
        for j in range(l[0],l[0]+l[2]):b[i][j]=n
    n+=1
b=sum(b,[])
for i in range(1,n):print(b.count(i))