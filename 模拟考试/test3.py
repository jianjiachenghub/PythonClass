import json
import jieba
def ReadTxt(Filename,coding):
    with open(Filename,encoding=coding) as file:
        text = file.read()
        words = jieba.lcut(text)
        count = {}
        for word in words:
            if len(word)== 1:
                continue
            else:
                count[word] = count.get(word,0)+1
        print(count)
        items = list(count.items())
        items.sort(key=lambda x:x[1],reverse=True)
        x = dict(items)
        print(x)
        xjson = json.dumps(x)
        print(xjson)
        with open('x.json','w',encoding= "utf-8") as file:
            json.dump(x,file,ensure_ascii=False)
ReadTxt('./西游记.txt',coding='gbk')