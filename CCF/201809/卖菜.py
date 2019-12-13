n = int(input())
lists = list(map(int,input().split()))
newlists = []
for i in range(0,n):
    if i ==0:
        newlists.append((lists[0]+lists[1])//2)
    elif i==n-1:
        newlists.append((lists[n-1]+lists[n-2])//2)
    else:
        newlists.append((lists[i]+lists[i+1]+lists[i-1])//3)
for i in newlists:
    print(i,end=" ")