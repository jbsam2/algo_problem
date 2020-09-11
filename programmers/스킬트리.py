def solution(skill, skill_trees):
    answer=0
    for i in skill_trees:
        l=[];f=1
        for j in range(len(i)):
            if i[j] in skill:l+=[i[j]]
        for j in range(len(l)):
            if l[j]!=skill[j]:f=0;break
        if f:answer+=1
    return answer