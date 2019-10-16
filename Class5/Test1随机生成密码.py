import random
list = []
for i in range(ord('a'),ord('z')+1):
    list.append(chr(i))
for i in range(ord('0'),ord('9')+1):
    list.append(chr(i))
for i in range(0,10):
    str = random.choices(list,k=8)
    str = ''.join(str)
    print((str))

