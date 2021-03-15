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




import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st