for t in range(int(input())):
    w=input()
    for i in range(len(w)//2):
        if w[i]!=w[-1-i]:print(f'#{t+1} 0');break
    else:print(f'#{t+1} 1')