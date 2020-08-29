def solution(n, arr1, arr2):
    answer = []
    ret=map(lambda x:x[2:].zfill(n),map(bin,map(lambda x,y:x|y,arr1,arr2)))
    for i in ret:
        tmp=''
        for j in i:tmp+=' ' if j=='0' else '#'
        answer.append(tmp)
    return answer