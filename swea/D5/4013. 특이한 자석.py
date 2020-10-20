for t in range(int(input())):
    n=int(input());ret=0
    g=[[*map(int,input().split())]for _ in range(4)]
    for _ in range(n):
        idx,m=map(int,input().split());idx-=1;r=[(idx,m)]
        tmp=m
        for i in range(idx,0,-1):
            if g[i-1][2]!=g[i][6]:tmp*=-1;r+=[(i-1,tmp)]
            else:break
        tmp=m
        for i in range(idx+1,4):
            if g[i][6]!=g[i-1][2]:tmp*=-1;r+=[(i,tmp)]
            else:break
        for idx,m in r:
            if m==1:g[idx]=[g[idx][-1]]+g[idx][:-1]
            elif m==-1:g[idx]=[g[idx][1:]]+[g[idx][0]]
    for i in range(4):ret+=g[i][0]*2**i
    print(f'#{t+1}',ret)


#######################################################################
def left_magnets(cur,rot):
    res = []
    if cur == 0:
        return res
    else:
        for i in range(cur-1,-1,-1):
            if magnets[i+1][6] != magnets[i][2]:
                res.append([i,rot])
                rot *= -1
            else:
                break
        return res
 
 
def right_magnets(cur,rot):
    res = []
    if cur == 3:
        return res
    else:
        for i in range(cur+1,4):
            if magnets[i-1][2] != magnets[i][6]:
                res.append([i,rot])
                rot *= -1
            else:
                break
        return res
 
 
def rotation(idx,rot):
 
    if rot == 1:  # 시계방향
        magnets[idx] = [magnets[idx][7]] + magnets[idx][0:7]
    else:  # 반시계방향
        magnets[idx] = magnets[idx][1:8] + [magnets[idx][0]]
 
 
for t in range(1,int(input())+1):
    K = int(input())
    magnets = [list(map(int,input().split())) for _ in range(4)]
    commands = [list(map(int,input().split())) for _ in range(K)]
    for command in commands:
 
        left_magnets_command = left_magnets(command[0]-1,-command[1])
        right_magnets_command = right_magnets(command[0]-1,-command[1])
 
        rotation(command[0]-1,command[1])
 
        for c in left_magnets_command:
            rotation(c[0],c[1])
        for c in right_magnets_command:
            rotation(c[0], c[1])
 
    answer = 0
    for i in range(4):
        if magnets[i][0]:
            answer += 2**i
    print("#{} {}".format(t,answer))