for t in range(1,int(input())+1):
    s = input()
    leng = len(s)
    tmp1,tmp2,tmp3 = '','',''
    for i in range(leng):
        tmp1 += '..#.'
        tmp2 += '.#.#'
        tmp3 += '#.'+s[i]+'.'
    tmp1 += '.'
    tmp2 += '.'
    tmp3 += '#'
    print(tmp1)
    print(tmp2)
    print(tmp3)
    print(tmp2)
    print(tmp1)