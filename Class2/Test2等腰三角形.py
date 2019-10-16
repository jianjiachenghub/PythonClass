# 打印三角形
for i in range(1, 4):
    print(('*' * i).ljust(3, ' '))

for i in range(1, 6, 2):#从1开始一直加二
    print(('*' * i).center(5, ' '))

for i in range(1, 4):
    print(('*' * i).rjust(9, ' '))

for i in range(1,20,2):#从1开始一直加二
    print(('*'*i).center(30,' '))

for i in range(5,1,-1):  # 从1开始一直加二
    print((' ' * (5-i)),('*' * (2*i-1)))