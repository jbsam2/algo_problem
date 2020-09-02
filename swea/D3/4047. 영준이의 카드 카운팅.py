for t in range(int(input())):
    s=input();c={'S':13,'D':13,'H':13,'C':13}
    for i in range(0,len(s),3):
        c[s[i]]-=1
        if s.count(s[i:i+3])>1:c={0:'ERROR'};break
    print('#{}'.format(t+1),*c.values())



for t in range(1, 1+int(input())):
    strings = input()
    cnt = ['S', 'D', 'H', 'C']
    cnt_n = [13, 13, 13, 13]
    for i in range(4):
        cnt_n[i] -= strings.count(cnt[i])
    for i in range(4):
        if strings.count(strings[i*3:i*3+3]) > 1:
            print('#{} ERROR'.format(t))
            break
    else:
        print('#{} {} {} {} {}'.format(t, cnt_n[0], cnt_n[1], cnt_n[2], cnt_n[3]))