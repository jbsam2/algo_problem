c={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
def b(n):
    a=b=0;r=''
    for i in range(4):a=n//2;b=n%2;r=str(b)+r;n=a
    return r
for t in range(int(input())):
    n,m=input().split();n=''
    for i in m:n+=b(c[i])
    print('#{}'.format(t+1),n)