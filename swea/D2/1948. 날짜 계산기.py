t = int(input())

for tc in range(1,t+1):
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    date = list(map(int,input().split()))
    diff_month = sum(days[date[0]:date[2]+1])
    ret = diff_month - (date[1]-1) - (days[date[2]] - date[3])
    print(f'#{tc} {ret}')