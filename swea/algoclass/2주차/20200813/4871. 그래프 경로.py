def sol(n):
    chk[n]=True;r=0
    for i in board[n]:
        if not chk[i]:
            if i==g:return 1
            elif not r:r+=sol(i)
    return r

for t in range(int(input())):
    v,e=map(int, input().split());board=[[] for _ in range(v+1)];chk=[False for _ in range(v+1)];r=0
    for _ in range(e):
        s,f=map(int,input().split())
        board[s].append(f)
    s,g=map(int,input().split())
    print(f'#{t+1}',sol(s))