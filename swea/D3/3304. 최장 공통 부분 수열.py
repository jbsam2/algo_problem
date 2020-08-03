for t in range(int(input())):
    d = [[0 for _ in range(1001)]for _ in range(1001)]
    a,b=input().split()
    for i in range(1,len(a)+1):
        for j in range(1,len(b)+1):
            if a[i-1]==b[j-1]:
                d[i][j]=d[i-1][j-1]+1
            else:
                d[i][j]=max(d[i-1][j],d[i][j-1])
    print(f'#{t+1}',d[len(a)][len(b)])