def solution(m, n, board):
    x=board
    x2=[]

    for i in x: 
        x1=[]
        for i2 in i:
            x1.append(i2)
        x2.append(x1)

    point=1
    while point!=0:
        list=[]
        point=0
        for i in range(m-1):
            for j in range(n-1):
                if x2[i][j]==x2[i][j+1]==x2[i+1][j]==x2[i+1][j+1]!='팡!':
                    list.append([i,j])
                    point+=1

        for i2 in list:
            i,j=i2[0],i2[1]
            x2[i][j],x2[i][j+1],x2[i+1][j],x2[i+1][j+1]='팡!','팡!','팡!','팡!'

        for i3 in range(m):
            for i in range(m-1):
                for j in range(n):
                    if x2[i+1][j]=='팡!':
                        x2[i+1][j],x2[i][j]=x2[i][j],'팡!'

    cnt=0
    for i in x2:
        cnt+=i.count('팡!')
    return cnt