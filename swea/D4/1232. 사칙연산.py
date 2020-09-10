def s(i):return str(int(eval(s(n[i][0])+o[i]+s(n[i][1]))))if n[i]else o[i]
for t in range(10):
    o=[0];n=[0]
    for i in range(int(input())):a,b,*c=input().split();o+=[b];n+=[[*map(int,c)]]
    print(f'#{t+1}',s(1))