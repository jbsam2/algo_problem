x1, y1, x2, y2, N = map(int, input().split())
island = (map(int, input().split()) for _ in range(N))
island = [x + y*1j for x, y in island]
print(island)
int(input())
