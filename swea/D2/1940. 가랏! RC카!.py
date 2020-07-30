t = int(input())

for tc in range(1,t+1):
    controls = int(input())
    velo = dist = 0
    for control in range(controls):
        command = list(map(int, input().split()))
        if command[0] == 1:
            velo += command[1]
        elif command[0] == 2:
            velo -= command[1]
            if velo <= 0:
                velo = 0
        dist +=velo      
    print(f'#{tc} {dist}')