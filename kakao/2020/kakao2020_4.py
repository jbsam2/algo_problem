m={}
def h(q,w):
    if len(q)!=len(w):return 0
    for i in range(len(q)):
        if q[i]!='?' and q[i]!=w[i]:return 0
    return 1
def c(ws):
    for w in ws:
        for i in range(len(w)):
            k1=w[:i]+'?'*(len(w)-i)
            k2='?'*i+w[i:]
            m[k1]=m.get(k1,0)+1
            m[k2]=m.get(k2,0)+1
def solution(words, queries):
    answer=[];ml=0
    for w in words:ml=max(ml,len(w))
    if ml>1000:
        for q in queries:
            t=0
            for word in words:
                if h(q,word):t+=1
            answer+=[t]
    else:
        c(words)
        for q in queries:
            try:answer+=[m[q]]
            except:answer+=[0]
    return answer