list = []
while 1:
    x = int(input('请输入整数'))
    if x == 0:
        break
    list.append(x)
list.sort(reverse=True)
for i in list:
    print(i,end='')
