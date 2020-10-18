d=[1,1]
for i in range(int(input())):d[0],d[1]=d[1],d[0]+d[1]
print(d[0]%10007)