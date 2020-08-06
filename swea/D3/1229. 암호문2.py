for a in range(10):
    input();b=input().split();c=int(input());d=input().split()
    for i in range(c):
        e=d.pop(0);f=int(d.pop(0));g=d.pop(0)
        if e=="I":
            for j in range(int(g)):b.insert((f+j),d.pop(0))
        else:
            for j in range(int(g)):del b[f]
    print(f'#{a+1}',' '.join(b[:10]))