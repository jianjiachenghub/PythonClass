# 凯撒密码
word = input("输入信息：")
for i in word:
    if ord("a") <= ord(i) <= ord("z"):
        print(chr(ord("a")+(ord(i)-ord("a")+3)% 26), end='')
    else:
        print(i, end=' ')