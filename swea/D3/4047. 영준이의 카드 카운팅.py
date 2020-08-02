for t in range(1,int(input())+1):
    s=input()
    c={'S':13,'D':13,'H':13,'C':13}
    for i in range(0,len(s),3):
        c[s[i]]-=1
        if s.count(s[i:i+3])>1:
            c={0:'ERROR'}
            break
    print('#%i'%t,*c.values())