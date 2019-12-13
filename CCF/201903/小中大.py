n = int(input())
arr = list(map(int,input().split()))
big = max(arr)
small = min(arr)
middile = 0
if len(arr)%2!=0:
    middile = arr[n//2]
else:
    middile = (arr[n//2-1]+arr[n//2])/2
if middile-int(middile)==0:
    middile = int(middile)
print(big,middile,small)