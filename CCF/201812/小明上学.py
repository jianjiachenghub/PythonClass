light = list(map(int,input().split()))
n = int(input())
sum = 0
for i in range(0,n):
    id,time = list(map(int,input().split()))
    if id == 1:
        sum+=time
    elif id == 2:
        sum += light[0]+time
    elif id == 0:
        sum+=time
print(sum)

