n=input();a=0
if int(n)<10:n='0'+n
r=n
while 1:
    tmp=0
    for i in n:tmp+=int(i)
    a+=1;k=str(tmp);n=n[-1]+k[-1]
    if n==r:break    
print(a)