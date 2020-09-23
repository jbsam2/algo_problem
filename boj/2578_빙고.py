b=[];d={};a=[];c=0;f=0
for i in range(5):
    r=input().split();b+=[r]
    for j in range(5):d[r[j]]=(i,j)
for i in range(5):a+=input().split()
for i in a:
    f+=1;y,x=d[i];b[y][x]=0;c+=all([b[j][x]==0 for j in range(5)])+all([b[y][j]==0 for j in range(5)])
    if x==y:c+=all(b[j][j]==0 for j in range(5))
    if x+y==4:c+=all(b[j][4-j]==0 for j in range(5))
    if c>2:break
print(f)