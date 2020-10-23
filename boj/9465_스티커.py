for t in range(int(input())):
    n=int(input())
    s1=[*map(int,input().split())]
    s2=[*map(int,input().split())]
    x=s1[0];y=s2[0];z=0
    for i in range(1,n):x,y,z=max(y,z)+s1[i],max(x,z)+s2[i],max(x,y)
    print(max(x,y,z))