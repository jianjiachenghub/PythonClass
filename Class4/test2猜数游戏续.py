import random
a = random.randint(1,10)
c = 0
flag = True
while flag:
    b = input("输入预测值：")
    try:
        b = eval(b)
    except:
        print("输入格式错误，结束程序！")
    if isinstance(b,float):
        print("输入错误，必须输入整数！")
        continue
    elif isinstance(b,int):
        c = c+1
        if b>a:
            print("大了")
        elif b<a:
            print("小了")
        elif b==a:
            flag = False
print("预测{}次，你猜中了！".format(c))