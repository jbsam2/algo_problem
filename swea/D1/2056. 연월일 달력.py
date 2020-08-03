s=[0,31,28,31,30,31,30,31,31,30,31,30,31]
for t in range(1, int(input())+1): 
    ret='';c=input();y=int(c[:4]);m=int(c[4:6]);d=int(c[6:]) 
    ret='-1' if m>13 or m<1 or d>s[m] or d<1 else f'{c[:4]}/{c[4:6]}/{c[6:]}'
    print(f'#{t} {ret}')