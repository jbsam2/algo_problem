for t in range(int(input())):
    input();tree=[0];idx=1;a=0
    for i in map(int,input().split()):
        tree.append(i);j=idx
        while tree[j//2]>tree[j]:tree[j//2],tree[j]=tree[j],tree[j//2];j//=2
        idx+=1
    p=len(tree)-1
    while p>0:a+=tree[p//2];p//=2            
    print('#{}'.format(t+1),a)