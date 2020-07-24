def solution(gems):
    answer = [0, len(gems)]
    dgems = {x:0 for x in gems}
    l, r = 0, 0
    tmp = set()
    while 1:
        if len(tmp) == len(dgems):
            l += 1
            dgems[gems[l-1]] -= 1
            if dgems[gems[l-1]] == 0:
                tmp.remove(gems[l-1])
            if r - l < answer[1] - answer[0]:
                answer = [l, r]
        elif r == len(gems):
            break
        else:
            r += 1
            tmp.add(gems[r-1])
            dgems[gems[r-1]] += 1
    return answer