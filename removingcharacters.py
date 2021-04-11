st = input('Enter the string : ')
for i in st:
    if (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z'):
        print(i,end='')