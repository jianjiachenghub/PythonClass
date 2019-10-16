a = eval(input("输入第一个数"))
b = eval(input("输入第二个数"))
s = 0
if a>=b:
    max = a
    min = b
else:
    max = b
    min = a
print(min)
print(max)
while 1:
    shang = max/min
    r = max%min
    if r == 0:
        s = min
        print("最大公约数为{}".format(min))
        break
    max = min
    min = r
print("最大公倍数为{}".format(int(a*b/min)))

