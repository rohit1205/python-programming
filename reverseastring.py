st = input('Enter the string : ')
l=len(st)
ts=''
for i in range(0,l):
    ts=st[i]+ts
print(ts)