t = int(input())

for tc in range(1,t+1):
    time_list = list(map(int,input().split()))
    ret_hour = time_list[0] + time_list[2]
    ret_min = time_list[1] + time_list[3]
    if ret_min >= 60:
        ret_hour += 1
        ret_min -= 60
    if ret_hour > 12:
        ret_hour -= 12
    print(f'#{tc} {ret_hour} {ret_min}')