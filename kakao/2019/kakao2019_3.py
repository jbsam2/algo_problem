from itertools import chain,combinations

def get_all_subset(iterable):
    s=list(iterable)
    return chain.from_iterable(combinations(s,r) for r in range(len(s)+1))

def get_all_unique_subset(relation):
    subset_list=get_all_subset(list(range(0,len(relation[0]))))
    unique_list=[]
    for subset in subset_list:
        unique=True
        row_set=set()
        for i in range(len(relation)):
            row=''
            for j in subset:
                row+=relation[i][j]+'.'
            if row in row_set:
                unique=False
                break
            row_set.add(row)
        if unique:
            unique_list.append(subset)
    return unique_list
    
def solution(relation):
    unique_list=get_all_unique_subset(relation)
    unique_list=sorted(unique_list, key=lambda x: len(x))
    answer_list=[]
    for subset in unique_list:
        subset=set(subset)
        chk=True
        for j in answer_list:
            if j.issubset(subset):
                chk=False
        if chk==True:
            answer_list.append(subset)
    return len(answer_list)