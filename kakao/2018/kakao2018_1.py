def solution(n, arr1, arr2):
    answer = []
    com=list(map(lambda x,y:x|y,arr1,arr2))
    ret=list(map(lambda x:x[2:].zfill(n),list(map(bin,com))))
    for i in ret:
        tmp=''
        for j in i:
            x=' ' if j=='0' else '#'
            tmp+=x
        answer.append(tmp)
    return answer