def possi(x, y, is_beam, beam, pillar):
    if is_beam:
        return (pillar[x][y-1] or pillar[x+1][y-1]) or ((x>=1 and beam[x-1][y]) and beam[x+1][y])
    else:
        return y==0 or ((x>=1 and beam[x-1][y]) or beam[x][y]) or pillar[x][y-1]

def install(x, y, is_beam, beam, pillar, is_install):
    if is_beam:
        beam[x][y] = is_install
    else:
        pillar[x][y] = is_install

def chk(res, beam, pillar):
    for x, y, is_beam in res:
        if not possi(x, y, is_beam, beam, pillar):
            return 0
    return 1

def solution(n, build_frame):
    res = []
    beam = [[0]*(n+1) for _ in range(n+1)]
    pillar = [[0]*(n+1) for _ in range(n+1)]
    for x, y, is_beam, is_install in build_frame:
        if is_install:
            if possi(x, y, is_beam, beam, pillar):
                install(x, y, is_beam, beam, pillar, is_install)
                res.append([x, y, is_beam])
        else:
            install(x, y, is_beam, beam, pillar, is_install)
            if chk(res, beam, pillar):
                res.remove([x, y, is_beam])
            else:
                install(x, y, is_beam, beam, pillar, 1)
    return sorted(res)