fo = open("lex.txt", "r",encoding="utf-8")
print(fo)
#print("read",fo.read())
for item in fo:
    print("one:",item)
for item in fo:
    print("two:",item)