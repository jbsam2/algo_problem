import re,itertools
def solution(expression):
    olist=[[*x] for x in itertools.permutations([x for x in['*','-','+']if x in expression])]
    c=re.split(r'(\D)',expression);ret=[]
    for oset in olist:
        t=c[:]
        for o in oset:
            while o in t:i=t.index(o);t[i-1]=str(eval(t[i-1]+o+t[i+1]));t=t[:i]+t[i+2:]
        ret.append(abs(int(*t)))
    return max(ret)