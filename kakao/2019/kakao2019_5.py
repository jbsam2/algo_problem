import sys,copy
preorder=[];postorder=[]
def order(nodes,levels,curlevel):
    n=copy.deepcopy(nodes);cur=n.pop(0)
    preorder.append(cur[0])
    if n:
        for i in range(len(n)):
            if n[i][1][1]==levels[curlevel]:
                if n[i][1][0]<cur[1][0]:order([x for x in n if x[1][0]<cur[1][0]],levels,curlevel+1)
                else:order([x for x in n if x[1][0]>cur[1][0]],levels,curlevel+1)
    postorder.append(cur[0])

def solution(nodeinfo):
    sys.setrecursionlimit(10**4)
    levels=sorted([*{x[1] for x in nodeinfo}],reverse=True)
    nodes=sorted([*zip(range(1,len(nodeinfo)+1),nodeinfo)],key=lambda x:(-x[1][1],x[1][0]))
    order(nodes,levels,1)
    return [preorder,postorder]