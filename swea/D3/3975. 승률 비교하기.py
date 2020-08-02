r=[]
for t in range(1,int(input())+1):
    a,b,c,d = map(int,input().split())
    r+=[f"#{t} {'DRAW'if a/b==c/d else'ALICE'if a/b>c/d else'BOB'}"]
print('\n'.join(r))