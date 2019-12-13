import csv

data_list = []
def Prime(x):
    flag = True
    for i in range(2,x):
        if x%i == 0:
            flag = False
    return flag
def Sym_Data(ls):
    sum = 0
    for i in ls:
        sum = sum +i
    return sum



with open('./Test.csv') as csvfile:
    csvRead = csv.reader(csvfile)
    for line in csvRead:
        for x in line:
            if Prime(int(x)):
                data_list.append(int(x))
print(Sym_Data(data_list))