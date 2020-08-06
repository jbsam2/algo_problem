for t in range(int(input())):
    n,k=list(map(int,input().split()));l=[];g=['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
    for i in range(n):m,f,a=map(int,input().split());l.append(0.35*m+0.45*f+a*0.2)
    r=l[k-1];l.sort(reverse=True);d=l.index(r)//(n//10);print(f'#{t+1}',g[d])