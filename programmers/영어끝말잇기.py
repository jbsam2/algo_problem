def solution(n, words):
    d={i:0 for i in range(n+1)};prev_word='';prev_words=[];num=0;r=[]
    for word in words:
        if word not in prev_words and (prev_word=='' or prev_word[-1]==word[0]):
            d[num]+=1;num=(num+1)%n;prev_words.append(word);prev_word=word
        else:return [num+1,d[num]+1]
    else:return [0,0]