from itertools import permutations as perm
def leng(a,b):return abs(a[0]-b[0])+abs(a[1]-b[1])
for t in range(int(input())):
    n=int(input())
    c1,c2,h1,h2,*l=map(int,input().split())
    c=(c1,c2);h=(h1,h2)
    customers=[]
    ret=1<<32
    for i in range(n):
        customers.append((l[2*i],l[2*i+1]))
    for i in perm(customers):
        tmp=0
        tmp+=leng(c,i[0])
        tmp+=leng(i[-1],h)
        for j in range(1,len(i)):
            tmp+=leng(i[j],i[j-1])
        ret=min(ret,tmp)
    print(f'#{t+1}',ret)




for test in range(1, int(input())+1):
    N = int(input())
    info = list(map(int, input().split()))
    start = (info[0], info[1])
    end = (info[2], info[3])
    distance = [ [0]*N for _ in range(N) ]
    for i in range(N):
        for j in range(i+1, N):
            distance[i][j] = distance[j][i] = abs(info[2*i+4] - info[2*j+4]) + abs(info[2*i+5] - info[2*j+5])
  
    bitmask = [ [0]*N for _ in range(1<<N) ]      
    bitlen = [0]                                              
    for _ in range(N):
        bitlen = bitlen + [ num+1 for num in bitlen ]
  
    for num in range(N):
        bitmask[1<<num][num] = abs(start[0] - info[2*num+4]) +  abs(start[1] - info[2*num+5])
  
    for length in range(2, N+1):
        for idx in range(1, 1<<N):
            if bitlen[idx] != length: continue    
            members = [ i for i in range(N) if idx & (1<<i) ]   
            for member in members:
                shortcut = float('inf')
                for rest in members:
                    if rest == member: continue
                    shortcut = min(shortcut, bitmask[idx-(1<<member)][rest] + distance[rest][member])
                bitmask[idx][member] = shortcut
  
    ans = float('inf')
    for n in range(N):
        ans = min(ans, bitmask[-1][n]+abs(end[0]-info[2*n+4])+abs(end[1]-info[2*n+5]))
    print('#{} {}'.format(test, ans))