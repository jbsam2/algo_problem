for t in range(1,int(input())+1):
    n,q = map(int,input().split())
    box = [0 for i in range(n)]
    for i in range(q):
        l,r = map(int,input().split())
        for j in range(l,r+1):
            box[j-1] = i+1
    ret = ''
    for i in box:
        ret += str(i)+' '
    print(f'#{t} {ret}')