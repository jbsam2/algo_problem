from collections import Counter
n = int(input())
for num in range(1,n+1):
    tmp_num = str(num)
    cnt = Counter(tmp_num)
    cnt_369 = cnt['3']+cnt['6']+cnt['9']
    if  cnt_369:
        print('-'*cnt_369,end=' ')
    else:
        print(tmp_num,end=' ')