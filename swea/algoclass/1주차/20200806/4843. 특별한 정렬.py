for t in range(int(input())):
    n=int(input());a=sorted(list(map(int,input().split())));ret=''
    for i in range(5):ret+=str(a[len(a)-1-i])+' '+str(a[i])+ ' '
    print(f'#{t+1}',ret)