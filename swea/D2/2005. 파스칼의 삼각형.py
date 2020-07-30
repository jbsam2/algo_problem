pascal = [[1 for a in range(i)] for i in range(1,11)]
for i in range(2,10):
    for j in range(1,i):
        pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
t = int(input())
for tc in range(1,t+1):
    num = int(input())
    print('#%d'%tc)
    for i in range(num):
        for j in range(len(pascal[i])):
            print(pascal[i][j],end=' ')
        print()