def isShuSu( x ):
    flag = True
    for i in range(2, x):
        if x % i == 0:
            flag = False
    return flag

while 1:
    x = int(input("请输入大于2的数"))
    if x >= 2:
        flag = True
        for i in range(2, x):
            if isShuSu(i):
                print(i)
        break


