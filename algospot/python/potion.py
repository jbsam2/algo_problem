from fractions import gcd
from functools import reduce

for case in range(int(input())):
    n = int(input())
    R = list(map(int, input().split()))
    P = list(map(int, input().split()))
    g = reduce(gcd, R)
    U = [r//g for r in R]
    i = max(g, max((p-1)//u+1 for p, u in zip(P, U)))
    print(' '.join(map(str, (i*u - p for p, u in zip(P, U)))))
