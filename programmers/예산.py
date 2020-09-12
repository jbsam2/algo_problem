def solution(d, budget):
    tmp=cnt=0
    for i in sorted(d):
        tmp+=i
        if tmp>budget:break
        cnt+=1
    return cnt