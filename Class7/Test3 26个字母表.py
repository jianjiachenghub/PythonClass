def numlist():
    h=[]
    for i in range(1,27):
       h.append(i)
    return h
def charlist():
    h=[]
    j='A'
    for i in range(26):
        h.append(chr(ord(j)+i))
    return h
print(numlist())
print(charlist())
dict=dict(zip(numlist(),charlist()))
print(dict)
for i in dict.keys():
    if i%2==0:
        print(dict[i],end=' ')