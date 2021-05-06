def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    elif x < y:
        parent[y] = x
    else:
        parent[x] = y

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

# 부모 자기 가리키게
parent = [i for i in range(N+1)]

# i도시의 연결정보
for i in range(1, N+1):
    path = list(map(int, sys.stdin.readline().split()))
    # j도시와의 관계
    for j in range(1, len(path)+1):
        # 뭔가가 있다면
        if path[j-1]:
            # i와 j 합치기!
            union(i, j)

# 경로 저장
tour = list(map(int, sys.stdin.readline().split()))
# 모든 경로의 부모가 같다면 이 여행은 가넝
check = set([parent[i] for i in tour])

# check의 길이도 1일것
if len(check) == 1:
    print('YES')
else:
    print('NO')