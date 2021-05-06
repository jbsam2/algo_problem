t = int(input())
for _ in range(t):
    n = int(input())
    parent = [0]*(n+1)
    for i in range(n-1):
        a,b = map(int,input().split())
        parent[b] = a
    c,d = map(int,input().split())
    cparent = [c]
    dparent = [d]

    while parent[c]:
        cparent.append(parent[c])
        c=parent[c]
    while parent[d]:
        dparent.append(parent[d])
        d=parent[d]

    cdepth = len(cparent)-1
    ddepth = len(dparent)-1
    while cparent[cdepth] == dparent[ddepth]:
        cdepth-=1
        ddepth-=1
    print(cparent[cdepth+1])