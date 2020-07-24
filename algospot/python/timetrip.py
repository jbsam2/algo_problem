import sys
import gc
import collections
"""
v : number of galaxy
w : number of wormhole
e : wormhole graph
"""
def solve(v, w, e, reachable):
    gc.collect()
    dist = [987654321] * v

    dist[0] = 0
    for k in range(v-1):
        for here in range(v):
            for there, cost in e[here]:
                if dist[there] > dist[here] + cost:
                    dist[there] = dist[here] + cost

    for here in range(v):
        for there, cost in e[here]:
            if dist[there] > dist[here] + cost:
                if reachable[0][here] and reachable[here][1]:
                    return 987654321

    return dist[1]



for i in range(int(input())):
    v, w = map(int, input().split())
    e = [[]  for _ in range(v)]
    e_neg = [[] for _ in range(v)]
    reachable = [[False] * v for _ in range(v)]
    for i in range(v):
        reachable[i][i] = True

    for _ in range(w):
        i, j, value = map(int, input().split())
        e[i].append((j,value))
        e_neg[i].append((j,-value))
        reachable[i][j] = True

    for k in range(v):
        for i in range(v):
            for j in range(v):
                reachable[i][j] = reachable[i][j] or (reachable[i][k] and reachable[k][j])

    if not reachable[0][1] :
        print ('UNREACHABLE')
        continue


    ret1 = solve(v,w,e,reachable)
    ret2 = -solve(v,w,e_neg,reachable)
    max_value = 10**10
    if ret1 == 987654321:
        ret1 = 'INFINITY'
    if abs(ret2) == 987654321:
        ret2 = 'INFINITY'

    print (ret1, ret2)
