n=int(input())
x=[int(input().split()[1])for _ in range(6)]*2
i=x.index(max(x))
j=x.index(max(x[i-1],x[i+1]))
print(n*(x[i]*x[j]-x[i+3]*x[j+3]))