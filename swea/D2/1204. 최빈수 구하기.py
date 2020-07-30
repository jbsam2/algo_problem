t = int(input())

for c in range(t):
    tc = int(input())
    scores = list(map(int, input().split()))
    cnt_dict = {}
    for score in scores:
        if score in cnt_dict:
            cnt_dict[score] += 1
        else:
            cnt_dict[score] = 1
    max_cnt = 0
    max_cnt_score = 0
    for score, cnt in cnt_dict.items():
        if max_cnt < cnt:
            max_cnt = cnt
            max_cnt_score = score
        elif max_cnt == cnt:
            if max_cnt_score < score:
                max_cnt_score = score
    print(f'#{tc} {max_cnt_score}')