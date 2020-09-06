import re
def getscore(word,page):return re.sub('[^a-z]+','.',page.lower()).split('.').count(word.lower())

def solution(word, pages):
    answer=[];webpages={}
    for i,page in enumerate(pages):
        links=[]
        title=page.split('<meta property="og:url" content="https://')[1].split('"')[0]
        for link in page.split('<a href="https://')[1:]:links.append(link.split('"')[0])
        webpages[title]=[i,getscore(word,page),links,0]
    for page in webpages.values():
        for link in page[2]:
            try:webpages[link][3]+=page[1]/len(page[2])
            except:pass
    for page in webpages.values():answer.append((page[0],page[1]+page[3]))
    return sorted(answer,key=lambda x:(-x[1],x[0]))[0][0]