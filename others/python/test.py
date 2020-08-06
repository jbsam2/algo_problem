T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    result = list(list(map(int, input().split())) for _ in range(N))
 
# 오류 풀이
    arr = []
    for x in range(N-M+1):
        for y in range(N-M + 1):            
            total = 0
            for k in range(x, x+M):
                for j in range(y, y+M):
                    total += result[k][j]
            arr.append(total)    
    print(f'#{tc} {max(arr)}')