a = 7
c = 0
flag = True
while flag:
    b = eval(input("输入预测值："))
    c = c+1
    if b>a:
        print("大了")
    elif b<a:
        print("小了")
    elif b==a:
        flag = False
print(c)