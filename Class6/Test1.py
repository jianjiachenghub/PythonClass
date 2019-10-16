import jieba
txt = open("./三国演义.txt", "r", encoding='utf-8').read()
words = jieba.lcut(txt)
dict = {}
for i in words:
    dict[i]=0
for i in words:
    dict[i]=dict[i]+1
sorted(dict, key=dict.__getitem__)
print(dict)