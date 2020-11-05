for t in range(int(input())):
    s=[]
    for i in input():
        if i in s:s.remove(i)
        else:s.append(i)
    print(f'#{t+1}',''.join(sorted(s))if len(s) else 'Good')