for t in range(1,int(input())+1):
    n=int(input())
    a=''
    while len(a)!=n: a+=input().replace(' ','')
    m=0
    while str(m) in a:m+=1
    print(f'#{t}',m)