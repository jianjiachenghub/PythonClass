phoneDict = {}
while True:
    try:
        txt = open("contact.txt", "r", encoding="utf-8")
        for line in txt:
            line = line.replace("\n", "")
            keyValue = line.split(":")
            phoneDict[keyValue[0]] = keyValue[1]
    except FileNotFoundError:
        txt = open("contact.txt", "w", encoding="utf-8")
    print("欢迎进入通讯录")
    print("1.查询联系人信息")
    print("2.插入新的联系人")
    print("3.删除联系人信息")
    print("4.退出通讯录程序")
    number = int(input("请输入你要进行的操作:"))
    if number == 1:
        name = input("请输入联系人姓名：")
        try:
            print("{0} : {1}".format(name, phoneDict[name]))
        except KeyError:
            print("联系人不存在！")
    elif number == 2:
        name = input("请输入插入联系人姓名：")
        if name in phoneDict:
            print("联系人已存在！")
        else:
            phone = input("联系人不存在。请输入电话：")
            phoneDict[name] = phone
            print("联系人插入成功。")
    elif number == 3:
        name = input("请输入删除联系人姓名：")
        if name not in phoneDict:
            print("联系人不存在。")
        else:
            del phoneDict[name]
            print("联系人删除成功！")
    elif number == 4:
        txt.close()
        txt = open("contact.txt", "w", encoding="utf-8")
        for line in phoneDict.items():
            key, value = line
            txt.write(str(key + ":" + value + "\n"))
        txt.close()
        break
    else:
        print("输入指令不合法！")