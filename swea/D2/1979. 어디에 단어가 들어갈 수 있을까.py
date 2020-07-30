t = int(input())

for tc in range(1,t+1):
    n, k = map(int,input().split())
    board = [list(map(int, input().split())) for i in range(n)]
    row_cnt = 0
    col_cnt = 0
    ret = 0
    for i in range(n):
        for j in range(n):

            if board[i][j] == 1:
                row_cnt += 1
            else:
                if row_cnt == k:
                    ret += 1
                    row_cnt = 0
                else:
                    row_cnt = 0

            if board[j][i] == 1:
                col_cnt += 1
            else:
                if col_cnt == k:
                    ret += 1
                    col_cnt = 0
                else:
                    col_cnt = 0

        if row_cnt == k:
            ret += 1
            row_cnt = 0
        else:
            row_cnt = 0
            
        if col_cnt == k:
            ret += 1
            col_cnt = 0
        else:
            col_cnt = 0

    print(f'#{tc} {ret}')