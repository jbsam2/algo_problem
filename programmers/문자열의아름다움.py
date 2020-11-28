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



from collections import defaultdict

def solution(s):
    n = len(s)-1
    answer = n*(n+1)*(n+2)//6
    sonny, kane = defaultdict(int), list()
    prev, consec =  s[0], 0

    for i in s:
        if i != prev : kane.append((prev, consec)); consec=0
        consec +=1
        for x in range(1, consec+1): sonny[i*x] += 1
        prev = i
    kane.append((prev,consec))

    for letter, counts in kane:
        for x in range(1, counts+1):
            sonny[letter*x] -= counts-x+1
            answer -= sonny[letter*x]*(counts-x+1)  
        answer -= (counts*(counts-1)*(counts+1)//6)

    return answer