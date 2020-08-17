for t in range(int(input())):
    l,k=map(int,input().split());s=input();m=[[0]*(l) for _ in range(l)];d={}
    for i in range(l):
        for j in range(i+1,l):m[i][j]=1<<32
    for i in range(k):d[chr(97+i)]=min(map(int,input().split()))
    for p in range(1,l):
        i=0;j=p
        for _ in range(l-p):
            m[i][j]=min(m[i][j],m[i+1][j]+d[s[i]],m[i][j-1]+d[s[j]])
            if s[i]==s[j]:m[i][j]=min(m[i][j],m[i+1][j-1])
            i+=1;j+=1
    print(f'#{t+1}',m[0][l-1])