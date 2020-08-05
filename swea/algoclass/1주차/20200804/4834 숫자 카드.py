for t in range(int(input())):
    n = int(input())
    card = [int(i) for i in input()]
    cnt_lst = [0]*10

    for i in range(n):
        cnt_lst[card[i]] += 1

    max_index, max_num = 0,0
    for i in range(len(cnt_lst)):
        if cnt_lst[i] > max_index:
            max_index = cnt_lst[i]
            max_num = i
        elif cnt_lst[i] == max_index:
            if max_num < i:
                max_num = i

    print(f'#{t+1}',max_num,max_index)