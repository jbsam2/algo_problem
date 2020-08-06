d={"ZRO":0,"ONE":1,"TWO":2,"THR":3,"FOR":4,"FIV":5,"SIX":6,"SVN":7,"EGT":8,"NIN":9}
e={0:"ZRO",1:"ONE",2:"TWO",3:"THR",4:"FOR",5:"FIV",6:"SIX",7:"SVN",8:"EGT",9:"NIN"}
for t in range(int(input())):
    k=input();n=list(input().split());r=[]
    for i in n:r.append(d[i])
    print(f'#{t+1}')
    for i in sorted(r):
        print(e[i],end=' ')