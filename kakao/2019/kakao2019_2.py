def solution(N, stages):
    answer = []
    length=len(stages)
    for i in range(1,N+1):
        cnt=stages.count(i)
        if length==0:
            fail=0
        else:
            fail=cnt/length
        answer.append((i,fail))
        length-=cnt
    return [i[0]for i in sorted(answer,key=lambda t:t[1],reverse=True)]