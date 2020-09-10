def solution(s):
    answer = 0
    for i in range(len(s)):
        for l in range(1,len(s)-i+1):
            if s[i:i+l]==s[i:i+l][::-1]:answer=max(l,answer)
    return answer