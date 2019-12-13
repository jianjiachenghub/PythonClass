# 如果文件内容比较少的时候，以下两种方式都可以

with open('lex.txt') as f:
    # 当文件很大时，f.readlines()结果是一个很大的列表在内存中，机器就卡了
    for line in f.readlines():
        print(line, end='')

# 推荐使用这种方式
with open('lex.txt') as f:  # f是一个可迭代对象，就像老母鸡会下蛋一样
    for line in f:
# 文件内容很大时，使用这种方式每次内存中只有一行内容
        print(line, end='')
