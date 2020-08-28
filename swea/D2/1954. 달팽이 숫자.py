for t in range(int(input())):
    N = int(input())

    nums = [[0]*N for _ in range(N)]

    K = N #이동거리
    d = 1 #방향
    row = 0 #행
    col = 0 #열 (초기에는 수평이동이므로 -1)
    num = 1 #넣을 값

    while True:
        #수평이동
        for c in range(K):
            nums[row][col] = num
            col += d
            num+=1
        #수평이동 끝 이제 수직이동
        K -= 1
        if K == 0:
            break
        #수직이동
        for r in range(K):
            row += d
            nums[row][col] = num
            num +=1
        #수직이동이 끝 수평이동
        d *= -1
    print("#{}".format(t+1))
    for i in nums:print(*i)
###################################################################################################

for t in range(int(input())):
    n=int(input());b=[[0]*n for _ in range(n)];l=1;dx=[1,0,-1,0];dy=[0,1,0,-1];r=c=d=0
    while l<=n*n:
        b[r][c]=l;nr=r+dy[d];nc=c+dx[d];l+=1
        if 0<=nr<n and 0<=nc<n and b[nr][nc]==0:r,c=nr,nc
        else:d=(d+1)%4;r+=dy[d];c+=dx[d]
    print('#{}'.format(t+1))
    for i in b:print(*i)