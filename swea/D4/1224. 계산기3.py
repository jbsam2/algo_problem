l={'*':2,'+':1,'(':0};k={'*':2,'+':1,'(':3} 
for t in range(10):
    input();rev=[];s=[]
    for i in input():
        if i.isdigit():rev.append(i)
        elif i==')':
            while rev[-1]!='(':rev.append(s.pop())
            rev.pop()
        else:
            while s and k[i]<=l[s[-1]]:rev.append(s.pop())
            s.append(i)
    while s:rev.append(s.pop())
    for i in rev:
        if i.isdigit():s.append(int(i))
        elif i=='+':s.append(s.pop()+s.pop())
        elif i=='*':s.append(s.pop()*s.pop())
    print('#{}'.format(t+1),*s)

###############################################################################

for t in range(10):
    input();d=[];l=[]
    for i in input():
        if i.isdigit():l+=[int(i)]
        elif i==')':
            j=-1
            while d[j]!='(':
                if d[j]=='*':l[j-1]=l[j-1]*l[j];l.pop(j);d.pop(j)
                else:j-=1
            j=-1
            while d[j]!='(':
                if d[j]=='+':l[j-1]=l[j-1]+l[j];l.pop(j);d.pop(j)
                else:j-=1
            d.pop(-1)
        else:d+=[i]
    print('#{}'.format(t+1),*l)