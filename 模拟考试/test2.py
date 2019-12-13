strInput = input()
len = ord('z')-ord('a')
data = [0 for i in range(len+1)]
for i in strInput:
    if ord("a") <= ord(i) <= ord("z"):
        index = ord(i)-ord('a')
        data[index]+=1
maxs = max(data)
index = data.index(maxs)
move = ord('h')-(ord('a')+index)
for i in strInput:
    if ord("a") <= ord(i) <= ord("z"):
        new = ord(i) + move
        if new<ord('a'):
            new = new+len+1
        print(chr(new),end='')
    else:
        print(i,end='')
