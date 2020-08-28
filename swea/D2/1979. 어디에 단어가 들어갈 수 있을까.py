for t in range(int(input())):
    n,k=map(int,input().split());b=[[*map(int,input().split())]for _ in range(n)];r=c=a=0
    for i in range(n):
        for j in range(n):
            if b[i][j]:r+=1
            else:
                if r==k:a+=1;r=0
                else:r=0
            if b[j][i]:c+=1
            else:
                if c==k:a+=1;c=0
                else:c=0
        if r==k:a+=1;r=0
        else:r=0
        if c==k:a+=1;c=0
        else:c=0
    print('#{} {}'.format(t+1,a))