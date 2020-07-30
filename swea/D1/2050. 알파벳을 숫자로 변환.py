alphabets = input()
alphabets.upper()
for char in alphabets:
    print(ord(char)-ord("A")+1, end=" ")