t = int(input())

for tc in range(1,1+t):
    n = int(input())
    board = []
    for i in range(n):
        board.append(list(map(int,input().split())))
        
    print(f'#{tc}')
    for y in range(n):
        for x in range(n):
            print(board[n-1-x][y],end='')
        print(' ',end='')
        for x in range(n):
            print(board[n-1-y][n-1-x],end='')
        print(' ',end='')
        for x in range(n):
            print(board[x][n-1-y],end='')
        print()