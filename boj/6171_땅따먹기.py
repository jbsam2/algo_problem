from sys import stdin
input = stdin.readline
n = int(input())
rect = [tuple(map(int,input().split())) for i in range(n)]
rect.sort()
stack = []
for r in rect:
    while stack and stack[-1][1] <= r[1]: stack.pop()
    stack.append(r)

def cross(x, y):
    ax, bx = hull[x]; ay, by = hull[y]
    return (by-bx) / (ax-ay)

def insert(a, b):
    hull.append((a,b))
    while len(hull) > 2 and cross(-2,-3) > cross(-1,-2): hull.pop(-2)

n = len(stack)
dp = [0]
hull = []
p = 0
for i in range(n):
    insert(stack[i][1], dp[-1])
    while p+1 < len(hull) and cross(p,p+1) <= stack[i][0]: p+= 1
    dp.append(hull[p][1] + hull[p][0]*stack[i][0])
print(dp[-1])