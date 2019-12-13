# 学习能力测试
x = 1.0
y = 1.0
for i in range(1,365):
    x += x * 0.01
print("努力学习的能力值为：{:.10f}".format(x))
for i in range(1,365):
    y -= y * 0.01
print("不努力学习的能力值为：{:.10f}".format(y))
z = 1.0
for i in range(1 , 365):
    if i % 7 in (6, 0):
        z -= z * 0.01
    else:
        z += z*0.01
print("五天学习两天不学习的结果是：{:.10f}".format(z))

print(list((6, 0)))
xx = 1+1.0
print(xx)
aa = '%.4f' % 1.232355
print(round(2/3,2))
print(aa)