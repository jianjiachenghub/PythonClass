m = int(input())
res = 0
n = 0
n1 = 0
sum2 = 0
queue = []
first = 0

def ifLen(index):
    if index>= len(queue):
        return index - len(queue)
    else:
        return  index

for i in range(0,m):
    num,*arr = map(int,input().split())
    index = 0
    count = 1
    for j in arr[1:]:
        if j>0:
            index = count
        count+=1
    if index:
        arr1 = arr[0:index]
        arr2 = arr[index:num]
        sum1 = sum(arr1)
        sum2 = sum(arr2)
        if sum1 == arr2[0]:
            queue.append(0)
            res += sum2
        else:
            n1 +=1
            queue.append(1)
            res+=sum2
    else:
        sum1 = sum(arr)
        res+=sum1

for item in range(0,len(queue)):
    sum1 = queue[ifLen(item)]+queue[ifLen(item+1)]+queue[ifLen(item+2)]
    if sum1 == 3:
        n = n+1

print(res,n1,n)
