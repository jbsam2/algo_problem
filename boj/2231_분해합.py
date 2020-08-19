n=int(input())
print([*[i for i in range(n)if n==i+sum(map(int,str(i)))],0][0])