def c(board,n,m):
    for i in board:
        for j in range(0,n+1-m):
            if i[j:j+m]==i[j:j+m][::-1]:
                return i[j:j+m]

for t in range(int(input())):
    n,m=map(int,input().split())
    board=[input()for _ in range(n)]
    for j in range(n):
        tmp = ''
        for i in range(n):
            tmp += board[i][j]
        board.append(tmp)
    #board+=list(zip(*board)) 세로축을 쪼개서 col을 추가해준다.
    print('#{} {}'.format(t+1,''.join(c(l,n,m))))