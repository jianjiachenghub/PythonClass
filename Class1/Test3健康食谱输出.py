diet = ['土豆', '鸡肉', '绿豆', '番茄', '鸭肉']
for i in range(5):
    for n in range(i + 1, 5):
        print(diet[i], diet[n], end=",      ")