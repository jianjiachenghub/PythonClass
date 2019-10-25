def isShuSu( x ):
    flag = True
    if x == 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            flag = False
    return flag
pingfang = lambda x:x*x
print(pingfang(10))
def list_prime(*args):
    print(args)
    for i in args:
        if isShuSu(int(i)):
            print(i)
string = input("请多项输入")
listargs = string.split(" ")
print(listargs)
list_prime(*listargs)