for t in range(10):
    input();s='({[<';f=')}]>';d=[];r=1
    for i in input():
        if i in s:d.append(i)
        else:
            if d.pop()!=s[f.find(i)]:r=0;break
    if len(d):r=0
    print('#{} {}'.format(t+1,r))