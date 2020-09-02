l={'*':2,'/':2,'+':1,'-':1,'(':0};k={'*':2,'/':2,'+':1,'-':1,'(':3}
rev=[];o=[];s=[]
for i in input():
    if i.isalpha():rev.append(i)
    elif i==')':
        while rev[-1]!='(':rev.append(o.pop())
        rev.pop()
    else:
        while o and k[i]<=l[o[-1]]:rev.append(o.pop())
        o.append(i)
while o:rev.append(o.pop())
print(''.join(rev))