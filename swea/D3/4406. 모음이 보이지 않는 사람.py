import re
for t in range(int(input())):print(f'#{t+1}',(re.sub('a|e|i|o|u','',input())))