# 시간초과 해결 못함

from itertools import combinations as c
def solution(orders, course):
    maxorder=0
    for i in orders:
        maxorder=max(maxorder,len(i))
    menus=set();d={}
    for i in orders:
        for j in [*i]:
            menus.add(j)
    menus=sorted(list(menus))
    for kinds in course:
        for combis in c(menus,kinds):
            for order in orders:
                cnt=0
                for i in combis:
                    if i in order:cnt+=1
                if cnt==kinds:
                    d[combis]=d.get(combis,0)+1
    t=[[]for _ in range(max(course)+1)]
    for i in course:
        for j in d.keys():
            if len(j)==i:t[i].append((''.join(j),d[j]))
        t[i]=sorted(t[i],key=lambda x:-x[1])
    answer=[]
    for i in course:
        if i>maxorder:continue
        _max=t[i][0][1]
        if _max<2:continue
        answer.append(t[i][0][0])
        for j in t[i][1:]:
            if j[1]==_max:answer.append(j[0])
    return sorted(answer)