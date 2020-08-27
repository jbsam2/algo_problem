def chk(s):
    cnt=0
    for i in s:
        if i=='(':cnt+=1
        else:
            if cnt==0:return 0
            cnt-=1
    return 1

def solution(p):
    if not p:return p
    rcnt=lcnt=0;u='';v=''
    for i in range(len(p)):
        if p[i]=='(':lcnt+=1
        else:rcnt+=1
        if lcnt==rcnt:u=p[:i+1];v=p[i+1:];break
    if chk(u):return u+solution(v)
    else:
        answer='('+solution(v)+')'
        for i in u[1:-1]:
            if i=='(':answer+=')'
            else:answer+='('
    return answer