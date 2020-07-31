for t in range(1,int(input())+1):
    num = list(map(int,input().split()))
    tmp = set()
    for i in range(len(num)-2):
        for j in range(i+1,len(num)-1):
            for l in range(j+1,len(num)):
                tmp.add(num[i]+num[j]+num[l])
    tmp2 = list(tmp)
    tmp2.sort(reverse=True)
    print(f'#{t} {tmp2[4]}')