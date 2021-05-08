from itertools import permutations as pm
n=int(input())
k=int(input())
print(len(set([''.join(i)for i in pm([input()for _ in range(n)],k)])))