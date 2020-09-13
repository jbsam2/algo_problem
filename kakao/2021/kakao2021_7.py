# 아직 오답

def solution(sales, links):
    n=len(sales);answer=0
    treemember=[[] for _ in range(n+1)]
    treeboss=[[] for _ in range(n+1)]
    for i in links:
        treemember[i[0]].append(i[1])
        treeboss[i[1]].append(i[0])
    tree=[]
    for i,j in enumerate(treemember):
        tree.append((i,j))
    tree=sorted(tree,key=lambda x:-len(x[1]))
    v=[1]+[0]*n
    while sum(v)!=n+1:
        t=tree.pop()
        tb=t[0]
        if v[tb]:continue
        v[tb]=1;answer+=sales[tb-1]
        for i in treemember[tb]:v[i]=1
        for i in treeboss[tb]:
            v[i]=1
            for j in treemember[i]:
                v[j]=1
    return answer