def sol(x):
    for y in range(98,0,-1):
        if x and arr[y][x-1]:
            while x and arr[y][x-1]:x-=1
        elif x<99 and arr[y][x+1]:
            while x<99 and arr[y][x+1]:x+=1
    return x
for t in range(10):input();arr=[list(map(int,input().split()))for _ in range(100)];print('#{} {}'.format(t+1,sol(arr[99].index(2))))