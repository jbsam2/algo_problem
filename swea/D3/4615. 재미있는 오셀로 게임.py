for t in range(1,int(input())+1):
    d = [0,1,-1]
    n,m = map(int,input().split())
    board = [[0]*(n+1) for i in range(n+1)]
    board[n//2][n//2] = 2
    board[n//2+1][n//2] = 1
    board[n//2][n//2+1] = 1
    board[n//2+1][n//2+1] = 2
    for m in range(m):
        y, x, z = map(int,input().split())
        board[y][x] = z
        for i in d:
            for j in d:
                ny = y + i
                nx = x + j
                c=0
                while not(i == j == 0) and  ny>0 and nx>0 and ny<n+1 and nx<n+1:
                    c+=1
                    if not board[ny][nx]:
                        break
                    if board[ny][nx]==z:
                        for p in range(c):
                            board[y+i*p][x+j*p] = z
                        break
                    ny += i
                    nx += j
    print(f'#{t}',sum(board,[]).count(1),sum(board,[]).count(2))