for t in range(10):
    input();b=[[*map(int,input().split())]for _ in range(100)];a=0
    for i in range(100):
        for j in range(99):
            if b[j][i]==1:
                if b[j+1][i]==0:b[j+1][i]=1
                elif b[j+1][i]==2:a+=1 
    print('#{}'.format(t+1),a)



for t in range(10):
    b=[''.join(i)for i in zip(*[''.join(input().split())for _ in range(int(input()))])];a=0
    for i in b:a+=i.replace('0','').count('12')
    print('#{}'.format(t+1),a)


for t in range(10):
    b=[''.join(i)for i in zip(*[''.join(input().split())for _ in range(int(input()))])];a=0
    for i in b:
        s=[]
        for j in i:
            if j=='1':s.append(j)
            elif s and j=='2':s.append(j)
        for j in range(len(s)-1):
            if s[j]=='1' and s[j+1]=='2':a+=1
    print('#{}'.format(t+1),a)