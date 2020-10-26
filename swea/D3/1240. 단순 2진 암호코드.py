c={'0001101':0,'0011001':1,'0010011':2,'0111101':3,'0100011':4,'0110001':5,'0101111':6,'0111011':7,'0110111':8,'0001011':9}
def d(s):
    for y in range(n):
        for x in range(m-1,-1,-1):
            if s[y][x]=='1':return s[y][x-55:x+1]
for t in range(int(input())):
    n,m=map(int,input().split());h=d([input() for _ in range(n)]);r=[]
    for i in range(0,len(h),7):r.append(c[h[i:i+7]])
    v=(r[0]+r[2]+r[4]+r[6])*3+(r[1]+r[3]+r[5])+r[7]
    print(f'#{t+1}',0 if v%10 else sum(r))