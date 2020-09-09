n=input();a=0
if int(n)<10:n='0'+n
r=n
while 1:
    t=0
    for i in n:t+=int(i)
    a+=1;k=str(t);n=n[-1]+k[-1]
    if n==r:break    
print(a)

a=n=int(input());r=0
while(r<1)+a-n:n=(n%10)*10+(n*11//10)%10;r+=1
print(r)