for t in range(int(input())):
    n=int(input());b=[[*input().split()]for _ in ''*n];c=[*zip(*b)];print(f'#{t+1}')
    for i in range(n):print(''.join(c[i][::-1]),''.join(b[::-1][i][::-1]),''.join(c[::-1][i]))