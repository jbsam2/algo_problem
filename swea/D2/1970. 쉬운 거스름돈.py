for tc in range(1,int(input())+1):
    num = int(input())
    money_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    money_dict = dict.fromkeys(money_list, 0)
    for i in money_list:
        money_dict[i] += num // i
        num %= i
    print(f'#{tc}')
    for i in money_list:
        print(money_dict[i], end=' ')
    print()