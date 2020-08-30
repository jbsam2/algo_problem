def solution(n,weak,dist):
    dist.sort(reverse=True);q=[weak];v=set();v.add(tuple(weak))
    for i,d in enumerate(dist):
        for _ in range(len(q)):
            cur=q.pop(0)
            for p in cur:
                s=p;f=(p+d)%n;tmp=tuple(filter(lambda x:x<s or x>f,cur)if s<f else filter(lambda x:x<s and x>f,cur))
                if len(tmp)==0:return i+1
                elif tmp not in v:v.add(tmp);q.append(list(tmp))
    return -1