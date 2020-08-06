for t in range(int(input())):
    w=input()
    if w==w[::-1]:print(f'#{t+1}',1)
    else:print(f'#{t+1}',0)