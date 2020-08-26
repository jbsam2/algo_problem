ans=[]
def sol(cnt,ret,plus,minus,multy,div):
    global ans
    if cnt==n:ans.append(ret)
    if plus: sol(cnt+1,ret+a[cnt],plus-1,minus,multy,div)
    if minus: sol(cnt+1,ret-a[cnt],plus,minus-1,multy,div)
    if multy: sol(cnt+1,ret*a[cnt],plus,minus,multy-1,div)
    if div: sol(cnt+1,int(ret/a[cnt]),plus,minus,multy,div-1)
    
n=int(input());a=list(map(int,input().split()));s=list(map(int,input().split()));sol(1,a[0],s[0],s[1],s[2],s[3])
print(max(ans),min(ans))