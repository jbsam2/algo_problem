def solution(board, moves):
    basket=[0]
    answer=0
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1]!=0:
                basket.append(board[j][i-1])
                board[j][i-1]=0

                if basket[-1]==basket[-2]:
                    basket.pop(-1)
                    basket.pop(-1)
                    answer+=2     
                break
    return answer