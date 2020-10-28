z={'211':0,'221':1,'122':2,'411':3,'132':4,'231':5,'114':6,'312':7,'213':8,'112':9}
def r(a,b,c):m=min(a,b,c);a//=m;b//=m;c//=m;return str(a)+str(b)+str(c)              
for t in range(int(input())):
    n,m=map(int,input().split());f=[];v=[];ans=0;d=[input() for _ in range(n)];h=['']*n
    for i in range(n):
        for j in range(m):h[i]+=bin(int(d[i][j],16))[2:].zfill(4)
    for y in range(n):
        a=b=c=0
        for x in range(4*m-1,-1,-1):
            if a==0 and b==0 and h[y][x]=='1':c+=1
            elif c and a==0 and h[y][x]=='0':b+=1
            elif c and b and h[y][x]=='1':a+=1
            if a and h[y][x]=='0':f.append(z[r(a,b,c)]);a=b=c=0
            if len(f)==8:
                f=f[::-1];l=(f[0]+f[2]+f[4]+f[6])*3+(f[1]+f[3]+f[5])+f[7]
                if l%10==0 and f not in v:ans+=sum(f)
                v.append(f);f=[]
    print(f'#{t+1}',ans)