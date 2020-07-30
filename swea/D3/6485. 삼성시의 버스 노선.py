tc = int(input())

for t in range(1, tc+1):
	n = int(input())
	a = []
	b = []
	c = []
	for i in range(n):
		tmp1, tmp2 = map(int,input().split())
		a.append(tmp1)
		b.append(tmp2)
	p = int(input())
	print(f'#{t}',end = ' ')
	for i in range(p):
		c = int(input())
		cnt = 0
		for i in range(n):
			if a[i] <= c and c <= b[i]:
				cnt += 1
		print(cnt,end = ' ')
	print()