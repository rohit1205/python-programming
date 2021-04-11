a=(input('Enter your string\n'))
b=int(input("Enter the part size"))
strlen=len(a)
if strlen%b!=0:
    print("Enter a valid part size")
else:
    partsize=strlen/b
    n=0
    for i in a:
        if n%b==0:
            print()
        print(i,end='')
        n=n+1