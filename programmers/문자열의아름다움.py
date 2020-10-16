def solution(s):
    l = len(s)
    allsum = [[0]*(len(s)+1) for i in range(26)]
    allcnt = [[0]*(len(s)+1) for i in range(26)]
    prev = '0'
    cnt = 0
    res = 0
    for i,c in enumerate(s):
        k = int(i*(i+1)/2)
        if prev == c:
            cnt+=1
        else:
            prev = c
            cnt = 1
        ii = ord(c)-ord('a')

        idx = cnt

        while idx:
            k -= allsum[ii][idx]
            k += cnt*allcnt[ii][idx]
            idx -= idx&-idx

        idx = l
        while idx:
            k -= cnt*allcnt[ii][idx]
            idx -= idx&-idx

        idx = cnt
        while idx <= l:
            allsum[ii][idx]+=cnt
            allcnt[ii][idx]+=1
            idx += idx&-idx
        res += k
    return res