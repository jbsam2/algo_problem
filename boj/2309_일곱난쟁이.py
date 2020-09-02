l=[]
for _ in range(9):l.append(int(input()))
r=sum(l);l.sort()
for i in range(9):
    for j in range(i+1,9):
        if r-l[i]-l[j]==100:
            for k in range(9):
                if k==i or k==j:continue
                else:print(l[k])
            exit()