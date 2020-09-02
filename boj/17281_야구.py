from itertools import permutations as p
u=input;a=0;b=[[*map(int,u().split())]for _ in'a'*int(u())]
for i in p(range(1,9),8):
    i=[*i];i.insert(3,0);c=0;s=0
    for player in b:
        out=0;first,second,third=0,0,0
        while out<3:
            k=player[i[c]]
            if k==0:out+=1
            if k==1:s+=third;first,second,third=1,first,second
            if k==2:s+=second+third;first,second,third=0,1,first
            if k==3:s+=first+second+third;first,second,third=0,0,1
            if k==4:s+=first+second+third+1;first,second,third=0,0,0
            c=(c+1)%9
    a=max(a,s)
print(a)