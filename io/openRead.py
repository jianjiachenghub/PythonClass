# 每次read都是从上次读完的地方开始的 所以后面为空
fo = open("lex.txt", "r",encoding="utf-8")
print(fo)
print("read",fo.read())
print("read",fo.readline())
print("read",fo.readlines())