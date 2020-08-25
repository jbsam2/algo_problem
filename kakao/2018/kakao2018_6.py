def solution(m, n, board):
    x = [list(i) for i in board]
    flag = 1
    while flag:
        a = []
        flag = 0
        for i in range(m - 1):
            for j in range(n - 1):
                if x[i][j] == x[i][j + 1] == x[i + 1][j] == x[i + 1][j + 1] != 'b':
                    a.append([i,j])
                    flag = 1

        for k in a:
            i, j = k[0], k[1]
            x[i][j], x[i][j + 1], x[i + 1][j], x[i + 1][j + 1] = 'b', 'b', 'b', 'b'

        for k in range(m):
            for i in range(m - 1):
                for j in range(n):
                    if x[i + 1][j] == 'b':
                        x[i + 1][j], x[i][j] = x[i][j], 'b'

    return sum(x,[]).count('b')