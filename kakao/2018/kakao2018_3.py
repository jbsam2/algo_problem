from collections import deque

def sol(cachesize,cities):
	ans=0

	q=deque(maxlen=cachesize)

	for item in cities:
		item=item.lower()
		if item in q:
			ans+=1
			q.remove(item)
			q.append(item)
		else:
			ans+=5
			q.append(item)

	return ans

cachesize=int(input())
cities=input().split()
print(sol(cachesize,cities))
