d=[0]*12
n,k=map(int,input().split())
for _ in range(n):s,y=map(int,input().split());d[6*s+y-1]+=1
print(sum([(i+k-1)//k for i in d]))