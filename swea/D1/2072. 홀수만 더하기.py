t = int(input())
 
for tc in range(1, t + 1):
    ans = 0
    numbers = []
    numbers = input().split()
    for number in numbers:
        if int(number) % 2:
            ans += int(number)
    print(f'#{tc} {ans}')