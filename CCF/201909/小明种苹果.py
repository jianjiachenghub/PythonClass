m,n = map(int,input().split())
arr = []
min = 0
res = 0
index = 1
for i in range(0,m):
    num,*arr = map(int,input().split())
    sums = sum(arr)
    res += num+sums
    if sums<min:
        min = sums
        index = i+1

print(res,index,abs(min))
