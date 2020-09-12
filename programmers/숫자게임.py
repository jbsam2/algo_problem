def solution(A, B):
    answer = 0
    B.sort()
    for i in sorted(A):
        for j in B:
            if j>i:B.remove(j);answer+=1;break
    return answer