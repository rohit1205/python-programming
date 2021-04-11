a=input("Enter the string   ")
b=a.split()
for i in b:
    x=i.endswith('s')
    if x==1:
        print(i)