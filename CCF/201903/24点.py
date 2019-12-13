n = int(input())
arr = []
for i in range(0,n):
    res = eval(input().replace('/','//').replace('x','*'))
    if res == 24:
        arr.append('Yes')
    else:
        arr.append('No')
for i in arr:
    print(i)
