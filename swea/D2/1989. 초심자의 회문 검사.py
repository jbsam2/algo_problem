for t in range(int(input())):
    word=input()
    if word==word[::-1]:print(f'#{t+1}',1)
    else:print(f'#{t+1}',0)