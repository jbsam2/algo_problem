for t in range(10):
    n=int(input())
    box=list(map(int,input().split()))
    ret = 0
    for i in range(n):
        max_tmp = max(box)
        min_tmp = min(box)
        if max_tmp - min_tmp <=1:
            ret = max_tmp - min_tmp
            break
        box[box.index(max_tmp)] -= 1
        box[box.index(min_tmp)] += 1
    ret = max(box)-min(box)
    print(f'#{t+1}',ret)