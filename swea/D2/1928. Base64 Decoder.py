from base64 import b64decode
for t in range(int(input())):print(f'#{t+1}',b64decode(input()).decode("UTF-8"))