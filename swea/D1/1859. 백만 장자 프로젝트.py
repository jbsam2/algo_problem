t = int(input())
for tc in range(1,t+1):
    n = int(input())
    ret = 0
    input_list = list(map(int,input().split()))
    max_price = input_list[n-1]
    for i in input_list[n-2::-1]:
        if i <= max_price:
            ret += (max_price-i)
        else:
            max_price = i
    print(f'#{tc} {ret}')