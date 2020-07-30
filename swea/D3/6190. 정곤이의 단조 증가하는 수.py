def chk(n):
    tmp = 0
    for i in str(n):
        if int(i) < tmp:
            return False
        else:
            tmp = int(i)
    return True

for t in range(1, int(input())+1):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
 
    ans = -1
    for i in range(n-1):
        for j in range(i+1, n):
            tmp_num = arr[i] * arr[j]
            if ans >= tmp_num:
                break
            if chk(tmp_num):
                ans = max(ans, tmp_num)
    print(f'#{t} {ans}')