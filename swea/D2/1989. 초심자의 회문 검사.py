t = int(input())
for tc in range(1,t+1):
    word = input()
    size = len(word)
    for i in range(len(word)//2):
        if word[i] != word[-1-i]:
            print(f'#{tc} 0')
            break
    else:
        print(f'#{tc} 1')