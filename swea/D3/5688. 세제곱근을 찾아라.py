for t in range(1,int(input())+1):
    tmp = int(input())**(1/3)
    if abs(tmp - round(tmp,1)) > 0.00000001:
        print(f'#{t} -1')
    else:
        print(f'#{t} {int(round(tmp,1))}')