t = int(input())

for tc in range(1,t+1):
    n = int(input())
    board = [[0]*n for i in range(n)]
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    direction = 0
    row = 0
    col = 0
    num = 1
    while (num <= n*n):
        board[row][col] = num
        num += 1
        nrow = row + dy[direction]
        ncol = col + dx[direction]
        if 0<=nrow<n and 0<=ncol<n and board[nrow][ncol] == 0:
            row, col = nrow, ncol
        else:
            direction = (direction + 1) % 4
            row += dy[direction]
            col += dx[direction]
    print(f'#{tc}')
    for i in range(n):
        for j in range(n):
            print(board[i][j],end=' ')
        print()