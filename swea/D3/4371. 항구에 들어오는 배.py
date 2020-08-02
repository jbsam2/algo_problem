for t in range(1,int(input())+1):
    n = int(input())
    days = list(int(input())for i in range(n))    
    for i in days[1:]:
        for j in range(2*i-1,days[-1]+1,i-1):
            if j in days:
                days.remove(j)
    print(f'#{t} {len(days[1:])}')