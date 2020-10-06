import sys
sys.setrecursionlimit(1000000)
def preorder(inst,ined,postst,posted):
    if inst>ined:return
    i=idx[post[posted]]
    k=postst+i-1-inst
    print(post[posted],end=' ')
    preorder(inst,i-1,postst,k)
    preorder(i+1,ined,k+1,posted-1)

n=int(input())
inorder=[*map(int,input().split())]
post=[*map(int,input().split())]
idx={inorder[i]:i for i in range(n)}
preorder(0,n-1,0,n-1)