def sol(s):
    global cnt
    visit.append(s);cnt+=1
    for i in net[s]:
        if i not in visit:sol(i)

net=[[]for _ in range(int(input())+1)];visit=[];cnt=-1
for i in range(int(input())):s,e=map(int,input().split());net[s].append(e);net[e].append(s)
sol(1);print(cnt)