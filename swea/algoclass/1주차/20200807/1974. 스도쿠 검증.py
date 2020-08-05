def chk(l) :
    for i in range(1,10) :
        if not l.count(i) == 1:
            return 0
    return 1
for i in range(int(input())) :
    row = []
    square = []
    col = []
    cnt = 1
    for t in range(9):
        col.append([])
        square.append([])
    for j in range(9) :
        row.append(list(map(int,input().split())))
        for t in range(9) :
            col[t].append(row[j][t])
            square[t//3*3+j//3].append(row[j][t])
    for j in range(9) :
        if chk(col[j]) and chk(row[j]) and chk(square[j]) :
            continue
        else :
            cnt = 0
            break
    print(f'#{i+1} {cnt}')