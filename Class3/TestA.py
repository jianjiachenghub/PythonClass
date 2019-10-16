import random
# 用来存储数据

def createCode():
    list = ""
    # 总共四位
    for i in range(4):
        # 每位随机三种状态
        j = random.randrange(1,4)
        # 数字
        if j == 1:
            a = random.randrange(0,10)
            list = list + str(a)
        # 字母
        elif j == 2:
            a = chr(random.randrange(ord('a'),ord('z')+1))
            list = list + a
        else:
            a = chr(random.randrange(ord('A'),ord('Z')+1))
            list = list + a
    print(list)
    return list
flag = True
while flag:
   list =  createCode()
   inputList = input("输入验证码：")
   if list  == inputList:
       print("验证码输入正确")
       flag = False
   else:
       print("验证码输入错误")


