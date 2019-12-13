import json
import random
def getData(name):
    fr=open(name,'r')
    ls=[]
    n = 1
    for line in fr:
        line = line.replace("\n", "")
        if n == 1:
            for i in line.split('$'):
                ls.append(int(i))
            n = n+1
        elif n == 2:
            for i in line.split('*'):
                ls.append(int(i))
    return ls

def genNumber(data):
    len1 = len(data)
    data.sort()
    print(data)
    list = []
    for i in data:
        for j in range(i+1,len1):
            for k in range(j+1,len1):
                list.append(i*100+j*10+k)
    return list

def saveData(name,data):
    fr = open(name, 'a')
    n = len(data)
    fr.write("\n")
    fr.write("total:{}".format(n))
    fr.write("\n")
    ls = [str(i) for i in data]
    print(ls)
    fr.write(','.join(ls))

list1 = getData('data1.txt')
print(list1)
list2 = genNumber(list1)
saveData('data1.txt',list2)