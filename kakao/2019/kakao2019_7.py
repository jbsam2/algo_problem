import numpy as np
def solution(board):
    answer = 0

    blocks = {}
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if col:
                if col not in blocks:
                    blocks[col] = {"left": 51, "right": -1, "top": 51, "bottom" : -1, "coords" : []}
                blocks[col]["left"] = min(blocks[col]["left"], j)
                blocks[col]["right"] = max(blocks[col]["right"], j)
                blocks[col]["top"] = min(blocks[col]["top"], i)
                blocks[col]["bottom"] = max(blocks[col]["bottom"], i)
                blocks[col]["coords"].append([i, j])

    board = np.array(board)

    flag = 1
    while flag:
        flag = 0
        for block_key in blocks:
            can_remove = 1
            block = blocks[block_key]
            zeros = 0
            for i in range(block["top"], block["bottom"]+1):
                for j in range(block["left"], block["right"]+1):
                    if board[i][j] == 0:
                        zeros+=1
                        if board[:i,j].any():
                            can_remove = 0
                            break
                if not can_remove:
                    break
            if can_remove and zeros == 2:
                for coord in blocks[block_key]["coords"]:
                    board[coord[0]][coord[1]] = 0
                del blocks[block_key]
                flag = 1
                answer += 1
                break
    return answer