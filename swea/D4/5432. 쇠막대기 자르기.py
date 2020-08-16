for t in range(int(input())):
    a=c=k=0
    for i in input():
        j=')'>i
        c+=2*j-1
        a+=(j or c)*k
        k=j        
    print(f'#{t+1}',a)