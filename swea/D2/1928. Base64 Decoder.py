from base64 import b64decode

t = int(input())
for tc in range(1,t+1):
    print(f'#{tc} {b64decode(input()).decode("UTF-8")}')