n=int(input())
l=[int(input().split()[1])for _ in range(6)]*2
i=l.index(max(l))
j=l.index(max(l[i-1],l[i+1]))
print(n*(l[i]*l[j]-l[i+3]*l[j+3]))