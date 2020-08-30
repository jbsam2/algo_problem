for t in range(int(input())):
    n=int(input());b=[[*input().split()]for i in range(n)];l=[[*zip(*reversed(b))]]
    for _ in range(2):l+=[[*zip(*reversed(l[-1]))]]
    print(f'#{t+1}')
    for j in range(n):
        for i in range(3):print(''.join(l[i][j]),end=' ')
        print()


for t in range(int(input())):
    n=int(input());b=[[*input().split()]for _ in ''*n];c=[*zip(*b)];print(f'#{t+1}')
    for i in range(n):print(''.join(c[i][::-1]),''.join(b[::-1][i][::-1]),''.join(c[::-1][i]))