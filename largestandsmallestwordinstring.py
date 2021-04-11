st = input('Enter the string : ')
st2=st.split()
small=large=st2[0]
for k in range(0, len(st2)):
    if (len(small) > len(st2[k])):
        small = st2[k]
    if (len(large) < len(st2[k])):
        large = st2[k]
print("Smallest word: " + small)
print("Largest word: " + large)