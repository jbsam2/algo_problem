def solution(board):
    answer=0;blocks={}
    for i,r in enumerate(board):
        for j,c in enumerate(r):
            if c:
                if c not in blocks:blocks[c]={'t':51,'b':-1,'l':51,'r':-1,'c':[]}
                blocks[c]['t']=min(i,blocks[c]['t'])
                blocks[c]['b']=max(i,blocks[c]['b'])
                blocks[c]['l']=min(j,blocks[c]['l'])
                blocks[c]['r']=max(j,blocks[c]['r'])
                blocks[c]['c'].append((i,j))
    rkey=1
    while rkey:
        rkey=0
        for blkey,block in blocks.items():
            rmkey=1;z=0
            for i in range(block['t'],block['b']+1):
                for j in range(block['l'],block['r']+1):
                    if board[i][j]==0:
                        z+=1
                        for k in range(i):
                            if board[k][j]:rmkey=0;break
                        if rmkey==0:break
                if rmkey==0:break
            if z==2 and rmkey:
                for i in block['c']:board[i[0]][i[1]]=0
                del blocks[blkey];rkey=1;answer+=1;break
    return answer