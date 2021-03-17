for t in range(int(input())):
    n = int(input())
    m = []
    ps = []
    for r in range(n):
        l = list(map(int, input().split()))
        m.append(l)
        if 0 < r < n - 1:
            for c in range(1, n - 1):
                if l[c]:
                    ps.append((r, c))
    ans = [0, n * n]
    st = [(0, 0, 0, m)]
    while st:
        i, core, wire, m = st.pop()
        if i == len(ps):
            if core > ans[0] or (core == ans[0] and wire < ans[1]):
                ans = [core, wire] 
        elif len(ps) - i + core > ans[0] or (len(ps) - i + core == ans[0] and wire <= ans[1]):
            st.append((i + 1, core, wire, [l[:] for l in m])) 
            for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                r, c = ps[i]
                r += dr
                c += dc
                wire2 = wire
                m2 = [l[:] for l in m]
                while 0 <= r < n and 0 <= c < n and m[r][c] == 0:
                    m2[r][c] = 1
                    wire2 += 1
                    r += dr
                    c += dc
                if r == -1 or r == n or c == -1 or c == n:
                    st.append((i + 1, core + 1, wire2, m2))
    print(f'#{t+1}',ans[1])