dx=[1,-1,-1,1];dy=[1,1,-1,-1]
def sol(y,x,d,r):
    global a
    if not (-1<y<n and -1<x<n) or d>3:return
    if d==3 and (y,x)==(i,j):a=max(r,a);return
    if v[b[y][x]]:return
    v[b[y][x]]=1;ny,nx=y+dy[d],x+dx[d];sol(ny,nx,d,r+1);sol(ny,nx,d+1,r+1);v[b[y][x]]=0
for t in range(int(input())):
    n=int(input());b=[[int(x)for x in input().split()]for y in range(n)];a=-1;v=[0]*101
    for i in range(n-2):
        for j in range(1,n-1):sol(i,j,0,0)
    print(f'#{t+1}',a)



def my_calc():
    for length in range(N - 1, 1, -1):
        for i in range(1, length):
            j = length - i
            for r in range(i, N - j):
                for c in range(N - i - j):
                    # 출발
                    visited = [False] * 101
                    y, x = r, c
                    for d in range(4):  # 방향 전환
                        n = j if d % 2 else i
                        for _ in range(n):  # 직진
                            y, x = y + dy[d], x + dx[d]
                            if not visited[MAP[y][x]]:
                                visited[MAP[y][x]] = True
                            else:  # 중복이면 다음 출발로
                                break
                        else:
                            continue
                        break
                    else:  # 한바퀴 완주하면
                        return length * 2
    return -1

dx = [1, 1, -1, -1]
dy = [-1, 1, 1, -1]

for t in range(int(input())):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{t+1}', my_calc())