a=2;b=6;L=[2,6]
for i in range(2,205):a,b=b,(b*6-a*4)%1000;L.append(b)
for i in range(int(input())):
    n=int(input())
    if n>100:n=n%100+100
    s=str(L[n]-1);s='0'*(3-len(s))+s;print('Case #'+str(i+1)+':',s)