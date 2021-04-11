st = input('Enter the string : ')
l=len(st)
ts=''
for i in range(0,l):
    ts=st[i]+ts
if st==ts:
    print('The string is palindrome')
else:
    print('The string is not palindrome')