friends = sorted([int(i)for i in input()])
l = len(friends)
if l%2:
    print(friends[l//2])
else:
    print((friends[l//2 - 1] + friends[l//2])//2)