import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self,x,id,left_bound,right_bound):
        self.x=x
        self.id=id
        self.left_bound=left_bound
        self.right_bound=right_bound
        self.left_node=None
        self.right_node=None

preorder_ret=[]
postorder_ret=[]

def preorder(node):
    preorder_ret.append(node.id)
    if node.left_node is not None:
        preorder(node.left_node)
    if node.right_node is not None:
        preorder(node.right_node)
def postorder(node):
    if node.left_node is not None:
        postorder(node.left_node)
    if node.right_node is not None:
        postorder(node.right_node)
    postorder_ret.append(node.id)

def solution(nodeinfo):
    nodeinfo=[i+[idx+1] for idx,i in enumerate(nodeinfo)]
    nodeinfo=sorted(nodeinfo,key=lambda x:x[1], reverse=True)
    array=[]
    now=-1
    for i in nodeinfo:
        y=i[1]
        if y!=now:
            array.append([])
            now=y
        array[len(array)-1].append((i[0],i[2]))
    for i in range(len(array)):
        array[i]=sorted(array[i])
    root=Node(array[0][0][0],array[0][0][1],0,100000)
    node_list=[[]]
    node_list[0].append(root)
    for level in range(1,len(array)):
        node_list.append([])
        for data in array[level]:
            x=data[0]
            id=data[1]
            for parent_node in node_list[level-1]:
                if parent_node.left_bound<=x and parent_node.x>x:
                    now_node=Node(x,id,parent_node.left_bound,parent_node.x)
                    parent_node.left_node=now_node
                    node_list[level].append(now_node)
                    break
                elif parent_node.right_bound>=x and parent_node.x<x:
                    now_node=Node(x,id,parent_node.x,parent_node.right_bound)
                    parent_node.right_node=now_node
                    node_list[level].append(now_node)
                    break
    preorder(root)
    postorder(root)
    return [preorder_ret,postorder_ret]




    

import sys
sys.setrecursionlimit(10**6)

class Tree:
  def __init__(self,data,left_child=None,right_child=None):
    self.data=data
    self.left_child=left_child
    self.right_child=right_child

def maketree(nodeinfo,dic):
    #find root
    if len(nodeinfo)==0:
        return None
    nodeinfo.sort(key=lambda t:t[1],reverse=True)
    root=tuple(nodeinfo[0])
    nodenumber=dic[root]
    nodeinfo.pop(0)
    stan=root[0]
    leftinfo=[]
    rightinfo=[]
    for x in nodeinfo:
        if x[0]<stan:
            leftinfo.append(x)
        else:
            rightinfo.append(x)

    del dic[root]
    return Tree(nodenumber,maketree(leftinfo,dic),maketree(rightinfo,dic))

def preorder_traverse(tree,li):
    if tree == None: return
    li.append(tree.data)
    preorder_traverse(tree.left_child,li)
    preorder_traverse(tree.right_child,li)
    return li

def postorder_traverse(tree,li):
    if tree == None: return
    postorder_traverse(tree.left_child,li)
    postorder_traverse(tree.right_child,li)
    li.append(tree.data)
    return li

def solution(nodeinfo):
    dic=dict()
    for i,x in enumerate(nodeinfo):
        dic[tuple(x)]=i+1
    madetree=maketree(nodeinfo,dic)
    prelist=preorder_traverse(madetree,[])
    postlist=postorder_traverse(madetree,[])
    answer = [prelist,postlist]
    return answer