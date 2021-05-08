d=[0]*30;r=0
for i in range(int(input())):t,p=map(int,input().split());d[i+t]=max(d[i+t],r+p);r=max(r,d[i+1])
print(r)