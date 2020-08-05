p=[[1 for a in range(i)] for i in range(1,11)]
for i in range(2,10):
    for j in range(1,i):
        p[i][j]=p[i-1][j-1]+p[i-1][j]
for t in range(int(input())):
    n=int(input());print(f'#{t+1}')
    for i in range(n):
        for j in range(len(p[i])):
            print(p[i][j],end=' ')
        print()