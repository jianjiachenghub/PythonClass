def fact(n):
    sum =1
    for i in range(1,n+1):
        sum*=i
    return sum
def sum(list):
    sum = 0
    for i in list:
        sum+=fact(i)
    return sum
n = input("请输入一个数：")
s = sum(range(0,int(n)+1))
print(s)
