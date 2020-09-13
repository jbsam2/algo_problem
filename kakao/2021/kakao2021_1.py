def solution(new_id):
    tmp=''
    for i in new_id.lower():
        if i.isalpha() or i in ['-','_','.'] or i.isdigit():
            tmp+=i
    tmp1=''
    for i in range(len(tmp)):
        if not tmp1 and tmp[i]=='.':continue
        if tmp[i]=='.' and tmp1[-1]=='.':continue
        tmp1+=tmp[i]
    if tmp1 and tmp1[-1]=='.':tmp1=tmp1[:-1]
    if not tmp1:tmp1='a'
    if len(tmp1)>15:
        tmp1=tmp1[:15]
        if tmp1[-1]=='.':tmp1=tmp1[:-1]
    if len(tmp1)<3:
        while len(tmp1)<3:tmp1+=tmp1[-1]
    return tmp1