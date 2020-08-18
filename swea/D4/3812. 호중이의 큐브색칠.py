for t in range(int(input())):
    X,Y,Z,A,B,C,N=map(int,input().split()) 
    x=[0]*N;y=[0]*N;z=[0]*N;xy=[0]*N;xyz=[0]*N
    for i in range(X):x[abs(i-A)%N]+=1
    for j in range(Y):y[abs(j-B)%N]+=1
    for k in range(Z):z[abs(k-C)%N]+=1 
    for i in range(N):
        for j in range(N):xy[(i+j)%N]+=(x[i]*y[j]) 
    for i in range(N):
        for j in range(N):xyz[(i+j)%N]+=(xy[i]*z[j]) 
    print(f'#{t+1}',*xyz)