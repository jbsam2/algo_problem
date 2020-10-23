for t in range(int(input())):
    n=int(input());a=0;g=[[*map(int,input().split())]for _ in range(4)]
    for _ in range(n):
        i,m=map(int,input().split());i-=1;r=[(i,m)];p=m
        for j in range(i,0,-1):
            if g[j-1][2]!=g[j][6]:p*=-1;r+=[(j-1,p)]
            else:break
        p=m
        for j in range(i+1,4):
            if g[j][6]!=g[j-1][2]:p*=-1;r+=[(j,p)]
            else:break
        for i,m in r:
            if m==1:g[i]=[g[i].pop()]+g[i]
            elif m==-1:g[i]+=[g[i].pop(0)]
    for i in range(4):a+=g[i][0]*2**i
    print(f'#{t+1}',a)


#######################################################################
# def left_magnets(cur,rot):
#     res = []
#     if cur == 0:
#         return res
#     else:
#         for i in range(cur-1,-1,-1):
#             if magnets[i+1][6] != magnets[i][2]:
#                 res.append([i,rot])
#                 rot *= -1
#             else:
#                 break
#         return res
 
 
# def right_magnets(cur,rot):
#     res = []
#     if cur == 3:
#         return res
#     else:
#         for i in range(cur+1,4):
#             if magnets[i-1][2] != magnets[i][6]:
#                 res.append([i,rot])
#                 rot *= -1
#             else:
#                 break
#         return res
 
 
# def rotation(idx,rot):
 
#     if rot == 1:  # 시계방향
#         magnets[idx] = [magnets[idx][7]] + magnets[idx][0:7]
#     else:  # 반시계방향
#         magnets[idx] = magnets[idx][1:8] + [magnets[idx][0]]
 
 
# for t in range(1,int(input())+1):
#     K = int(input())
#     magnets = [list(map(int,input().split())) for _ in range(4)]
#     commands = [list(map(int,input().split())) for _ in range(K)]
#     for command in commands:
 
#         left_magnets_command = left_magnets(command[0]-1,-command[1])
#         right_magnets_command = right_magnets(command[0]-1,-command[1])
 
#         rotation(command[0]-1,command[1])
 
#         for c in left_magnets_command:
#             rotation(c[0],c[1])
#         for c in right_magnets_command:
#             rotation(c[0], c[1])
 
#     answer = 0
#     for i in range(4):
#         if magnets[i][0]:
#             answer += 2**i
#     print("#{} {}".format(t,answer))