# 测试密码强弱
import re
userName = input("请输入账户名：")
passWord = input("请输入密码：" )

def judge(passWord):
    isIllegal = re.search(r'[^a-zA-Z0-9]', passWord)
    while isIllegal:
        passWord = input("密码含有非法字符请重新输入密码：")
    while not 16 > len(passWord) > 8:
        passWord = input("请输入8~16的密码：")
    haveNum = re.search(r'\d+', passWord)
    haveLowercaseLetters = re.search(r'[a-z]+', passWord)
    haveCapital = re.search(r'[A-Z]+', passWord)
    count = 0
    if haveNum:
        count += 1
    if haveLowercaseLetters:
        count += 1
    if haveCapital:
        count += 1
    if count == 1:
        print("密码强度较弱")
    if count == 2:
        print("密码强度中等")
    if count == 3:
        print("密码强度较强")

judge(passWord)

