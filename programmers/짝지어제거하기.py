def solution(s):
    a=[]
    for i in s:
        if not a:a.append(i);continue
        if i==a[-1]:a.pop()
        else:a.append(i)
    return 0 if a else 1