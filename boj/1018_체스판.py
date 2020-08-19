white=[
    "WBWBWBWB",
	"BWBWBWBW",
	"WBWBWBWB",
	"BWBWBWBW",
	"WBWBWBWB",
	"BWBWBWBW",
	"WBWBWBWB",
	"BWBWBWBW"
]
black=[
    "BWBWBWBW",
	"WBWBWBWB",
	"BWBWBWBW",
	"WBWBWBWB",
	"BWBWBWBW",
	"WBWBWBWB",
	"BWBWBWBW",
	"WBWBWBWB"
]
def wcount(y,x,c=0):
    for i in range(y,y+8):
        for j in range(x,x+8):
            if b[i][j]!=white[i-y][j-x]:c+=1
    return c
def bcount(y,x,c=0):
    for i in range(y,y+8):
        for j in range(x,x+8):
            if b[i][j]!=black[i-y][j-x]:c+=1
    return c
n,m=map(int,input().split());b=[input()for i in range(n)];r=1<<32
for i in range(n-7):
    for j in range(m-7):
        r=min(r,wcount(i,j),bcount(i,j))
print(r)