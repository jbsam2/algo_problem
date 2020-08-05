for t in range(10):
    n=int(input())
    board = []
    ans = 0
    for i in range(100):
        board.append(list(map(int,input().split())))
        ans = max(ans,sum(board[i]))
    tmp2 = tmp3 = 0
    for i in range(100):
        tmp1=[]
        for j in range(100):
            tmp1.append(board[j][i])
            if i==j:
                tmp2 += board[i][j]
            if i+j == 99:
                tmp3 += board[i][j]
        ans = max(ans,sum(tmp1))
    ans = max(ans,tmp2,tmp3)
    print(f'#{t+1}',ans)