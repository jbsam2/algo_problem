import re,itertools
def solution(expression):
    c=re.split(r'(\D)',expression);ret=[]
    for oset in [[*x]for x in itertools.permutations([i for i in['*','-','+']if i in expression])]:
        t=c[:]
        for o in oset:
            while o in t:i=t.index(o);t[i-1]=str(eval(t[i-1]+o+t[i+1]));t=t[:i]+t[i+2:]
        ret.append(abs(int(*t)))
    return max(ret)