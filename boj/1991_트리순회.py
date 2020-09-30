pre=lambda i:i+pre(l[i][0])+pre(l[i][1])if i!='.'else''
inorder=lambda i:inorder(l[i][0])+i+inorder(l[i][1])if i!='.'else''
post=lambda i:post(l[i][0])+post(l[i][1])+i if i!='.'else''
l={}
for i in range(int(input())):a,*b=input().split();l[a]=b
print(pre('A'))
print(inorder('A'))
print(post('A'))