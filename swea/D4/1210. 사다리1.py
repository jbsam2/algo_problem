def sol(x):
    for y in range(98,0,-1):
        if x and arr[y][x-1]:
            while x and arr[y][x-1]:x-=1
        elif x<99 and arr[y][x+1]:
            while x<99 and arr[y][x+1]:x+=1
    return x
for t in range(10):
    input();arr=[list(map(int,input().split()))for _ in range(100)]
    for j in range(100):
        if arr[99][j]==2:x=j
    print('#{} {}'.format(t+1,sol(x)))

def s(l):
    for i in range(100):
        if l[99][i]==2:x=i;break
    for i in range(98,0,-1):
        if x>0 and l[i][x-1]:
            while l[i][x-1] and x>0:x-=1
        elif x<99 and l[i][x+1]:
            while x<99 and l[i][x+1]:x+=1
    return x
for i in range(10):print("#"+input(),s([list(map(int,input().split())) for i in range(100)]))