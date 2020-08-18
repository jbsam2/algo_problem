for t in range(int(input())):
    s=input();r=1
    for i in range(1,len(s)+1):
        for j in range(len(s)-i+1):
            p=s[j:j+i]
            if p==p[::-1]:r=max(r,i)
    print(f'#{t+1}',r)