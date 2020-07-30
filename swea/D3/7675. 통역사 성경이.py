tc = int(input())
for t in range(1, tc+1):
    n = int(input())
    data = input().replace('!',' !').replace('.',' .').replace('?',' ?').split()
    count = 0
    res = ''
    for i in data:
        if i.isalpha() and i == i.capitalize():
            count += 1
        if i in '.!?':
            res += str(count) + ' '
            count = 0
    print(f"#{t} {res}")