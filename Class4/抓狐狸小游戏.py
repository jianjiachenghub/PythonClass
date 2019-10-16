import random
list1=[0,1,2,3,4]
a=0
b=0
huli=random.choice(list1)
while(True):
    print(huli)
    caishu=eval(input("请猜一个数："))
    a=a+1
    if(a==10):
        print("game over！")
        break
    if caishu not in list1:
        print("请输入0到4之间的数")
    if(huli==caishu):
        print("抓住了狐狸")
        break
    if(huli==0):
        huli=huli+1
        b=b+1
    elif(huli==4):
        huli=huli-1
        b=b+1
    elif(b%2==0):
        huli=huli+1
    elif(b%2!=0):
        huli=huli-1



