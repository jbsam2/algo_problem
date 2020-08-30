from itertools import product

def check(s1,s2):
    if len(s1)!=len(s2):return False
    for i in range(len(s1)):
        if s1[i]=='*':continue
        if s1[i]!=s2[i]:return False
    return True

def solution(user_id, banned_id):
    answer=set();n=len(banned_id)
    r=[[]for _ in range(n)]
    for i in range(n):
        for u in user_id:
            if check(banned_id[i],u):r[i].append(u)
    r=list(product(*r))
    for i in r:
        if len(set(i))==n:answer.add(''.join(sorted(set(i))))
    return len(answer)