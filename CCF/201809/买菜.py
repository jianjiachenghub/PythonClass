n = int(input())
list1 = []
list2 = []
for i in range(0,n):
    min,max1 = list(map(int,input().split()))
    for j in range(min,max1):
        list1.append(j)
for i in range(0,n):
    min,max1 = list(map(int,input().split()))
    for j in range(min,max1):
        list2.append(j)
m = max(list1[-1],list2[-1])+1
count = [0 for i in range(m) ]
for i in list1:
    count[i]+=1
for i in list2:
    count[i]+=1
print(count.count(2))



