def search():
    w = input("请输入要查询的单词:")
    fr = open("test.txt", 'r')
    dic = {}
    for line in fr.readlines():
        line = line.replace("\n", "")
        line = list(line.split(","))
        key = line[0]
        coment = line[1:]
        dic[key] = coment  #
    if w in dic.keys():
        print(dic[w])
    else:
        print("你要查询的单词不存在！")
    fr.close()
def add():
    ww = input("请输入你要添加的单词：")
    flag = 0
    dic = {}
    f = open("test.txt", 'r')
    for line in f.readlines():
        line = line.replace("\n", "")
        line = list(line.split(","))
        key = line[0]
        coment = line[1:]
        dic[key] = coment
        if ww in dic.keys():
            f.close()
            flag = 1
            print("输入的单词已经存在!")
            break
        else:
            f.close()
    if flag != 1:  # 如果输入的单词不存在，则进行汉语意思的输入，若有多个意思，则用英文逗号隔开
        fw = open("test.txt", 'a')
        mean = input("若有多个意思，则用英文逗号隔开:")
        fw.write(ww + ',' + mean + '\r\n')
        fw.close()
while True:
    str = input("您要查询、添加还是退出字典:")
    if str =="查询":
        search()
        continue
    elif str == "添加":
        add()
        continue
    elif str == "退出字典":
        print("程序已经退出!")
        break
