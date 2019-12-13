r,y,g = list(map(int, input().split()))
all = r+y+g
n = int(input())
sum = 0
def Judge(move):
    if 0<=move<r+y:
        return r+y-move
    else:
        return 0
for i in range(0, n):
    id,time = list(map(int, input().split()))
    if id==0:
        sum+=time
    elif id==2:
        move = (sum%all+y-time)%all
        sum+=Judge(move)
    elif id==1:
        move = (sum%all+y+r-time)%all
        sum += Judge(move)
    elif id==3:
        move = (sum % all + y + r + g - time) % all
        sum += Judge(move)
print(sum)






