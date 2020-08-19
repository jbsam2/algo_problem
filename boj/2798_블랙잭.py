from itertools import*
b=input().split()
print(max([sum(i)for i in combinations(map(int,input().split()),3)if sum(i)<=int(b[1])]))