t = int(input())
for tc in range(1,t+1):
    n, m = map(int,input().split())
    fly_map = [ [int(x) for x in input().split()] for y in range(n) ]
    max_fly = 0
    for y in range(n-m+1):
        for x in range(n-m+1):
            kill_fly = 0
            for i in range(m):
                for j in range(m):
                    kill_fly += fly_map[y+i][x+j]
            if kill_fly > max_fly:
                max_fly = kill_fly
    print(f'#{tc} {max_fly}') 