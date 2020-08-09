for t in range(int(input())):
    n=input();r=0
    for i in n:r+=int(i)
    print(f'#{t+1}','B' if (len(n)+((r-1)//9))%2 else 'A')