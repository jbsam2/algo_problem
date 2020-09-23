l=sorted([int(input())for _ in range(9)])
r=sum(l)
for i in range(9):
    for j in range(i+1,9):
        if r-l[i]-l[j]==100:
            for k in range(9):
                if k==i or k==j:continue
                else:print(l[k])
            exit()