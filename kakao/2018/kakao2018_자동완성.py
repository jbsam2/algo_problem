class Trie():
    def __init__(self):self.next=dict();self.value=0 
def solution(words):
    answer=0;tree=Trie()
    for word in words:
        subtree=tree
        for i,char in enumerate(word):
            subtree.value+=1
            if char not in subtree.next:subtree.next[char]=Trie()
            subtree=subtree.next[char]
            if i==len(word)-1:subtree.value+=1 
    for word in words:
        subtree=tree;cnt=0
        for i,char in enumerate(word):
            if subtree.value==1:answer+=cnt;break
            elif i==len(word)-1:answer+=cnt+1;break
            else:subtree=subtree.next[char];cnt+=1 
    return answer