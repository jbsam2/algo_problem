p=[0,1,1]
for i in range(3,101):p.append(p[i-2]+p[i-3])
for t in range(int(input())):print(f'#{t+1}',p[int(input())])