def solution(a):
    answer = -1
    cnt = [0]*len(a)
    for i in a:
        cnt[i] += 1
    for i in range(len(cnt)):
        if cnt[i] == 0: continue
        if cnt[i] <= answer: continue
        ret = j = 0
        while j < len(a) - 1:
            if a[j] != i and a[j+1] != i:
                j += 1
                continue
            if a[j] == a[j+1]:
                j += 1
                continue
            ret += 1
            j += 2
        answer = max(answer, ret)
    return 2*answer