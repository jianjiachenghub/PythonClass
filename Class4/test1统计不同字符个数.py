inp = input("请输入字符")
num = az = block = other = 0
for i in inp:
    if ord('0')<=ord(i)<=ord('9'):
        num = num+1
    elif ord('a')<=ord(i)<=ord('z'):
        az += 1
    elif ord(' ')==ord(i):
        block +=1
    else:
        other +=1
print("数字有{}个".format(num))
print("字母有{}个".format(az))
print("空格有{}个".format(block))
print("其他字符有{}个".format(other))

