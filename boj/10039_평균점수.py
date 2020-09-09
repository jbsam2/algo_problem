s=[]
for _ in range(5):
    n=int(input())
    if n<40:n=40
    s.append(n)
print(sum(s)//5)