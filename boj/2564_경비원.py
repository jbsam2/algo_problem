w,h=map(int,input().split())
l=w+h+w+h #벽의 둘레
s=[]
c=0
for i in range(int(input())+1):
    a,b=map(int,input().split())
    s.append([0,l-b,h+b,b,l-w-b][a]) #좌상단 꼭지점을 기준으로 반시계 방향으로 탐색을 할때 상대거리를 저장해준다.
for i in s[:-1]: #s[-1]은 경비원의 좌표이므로 그 이전 까지만 비교하면 된다
    t=abs(i-s[-1]) #경비원과 각 좌표간의 상대 거리를 계산
    c+=min(t,l-t) # 시계방향과 반시계 방향 탐색 중 짧은 거리를 더해준다.
print(c)