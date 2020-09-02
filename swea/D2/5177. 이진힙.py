class Tree:
    def __init__(self):
        self.l=[0]
    
    def sort(self,size):
        if size>1:
            if self.l[size]<self.l[size//2]:
                self.l[size],self.l[size//2]=self.l[size//2],self.l[size]
                self.sort(size//2)
    
    def append(self,num):
        size=len(self.l)
        self.l.append(num)
        self.sort(size)

    def my_sum(self,node):
        if node<2:return self.l[node]
        else:return self.l[node]+self.my_sum(node//2)

    def ret(self):
        last=len(self.l)-1
        if last>1:return self.my_sum(last//2)
        else:return 0

for t in range(int(input())):
    input();tree=Tree()
    for i in map(int,input().split()):tree.append(i)
    print('#{}'.format(t+1),tree.ret())