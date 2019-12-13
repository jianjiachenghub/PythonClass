import os
import json
myJSON = {
    'admin':'123',
    'test':'234',
    'bob':'23421321',
}
logout=0

print(("欢迎进入通讯录"))
print(("1.查询联系人信息"))
print(("2.插入新的联系人"))
print(("3.删除联系人信息"))
print(("4.退出通讯录程序"))

if not os.path.exists('contact.txt'):
    fileObject = open('contact.txt', 'w')
    jsObj = json.dumps(myJSON)
    fileObject.write(jsObj)
    fileObject.close()



while(logout==0):
    com=eval(input("请选择要进行的操作:"))
    js = fileObject.read()
    dic = json.loads(js)
    if com == 1:
        name=input("请输入用户名:")
        if name in dic.keys():
            print(dic[name])
        else:
            print("联系人不存在！")
    elif com == 2:
        name = input("请输入用户名:")
        if name in dic.keys():
            print(dic[name])
            print("用户已存在！")
            break
        else:
            tel=input("请输入电话:")
            user={name:tel}
            User=json.dumps(user)
            fileObject.write(User)
            fileObject.close()
            print("插入联系人成功!")
    elif com == 3:
        continue
    elif com == 4:
        break
    else:
        print("输入不合法！请重新输入")
print("谢谢你的使用")
