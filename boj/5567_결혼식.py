f=[[]for _ in range(int(input())+1)]
for _ in range(int(input())):a,b=map(int,input().split());f[a]+=[b];f[b]+=[a]
r=[i for i in f[1]]
for i in f[1]:r+=f[i]
print(len(set(r))-1)