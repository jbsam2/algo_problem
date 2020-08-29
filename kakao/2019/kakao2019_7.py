def solution(board):
    answer=0;blocks={}
    for i,r in enumerate(board):
        for j,c in enumerate(r):
            if c:
                if c not in blocks:
                    blocks[c]={'top':51,'bottom':-1,'left':51,'right':-1,'coords':[]}
                blocks[c]['top']=min(i,blocks[c]['top'])
                blocks[c]['bottom']=max(i,blocks[c]['bottom'])
                blocks[c]['left']=min(j,blocks[c]['left'])
                blocks[c]['right']=max(j,blocks[c]['right'])
                blocks[c]['coords'].append((i,j))
    rkey=1
    while rkey:
        rkey=0
        for blkey,block in blocks.items():
            rmkey=1;z=0
            for i in range(block['top'],block['bottom']+1):
                for j in range(block['left'],block['right']+1):
                    if board[i][j]==0:
                        z+=1
                        for k in range(i):
                            if board[k][j]:rmkey=0;break
                        if rmkey==0:break
                if rmkey==0:break
            if z==2 and rmkey:
                for i in block['coords']:board[i[0]][i[1]]=0
                del blocks[blkey]
                rkey=1;answer+=1;break
    return answer