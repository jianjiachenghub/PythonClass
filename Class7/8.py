def fact(n):
    s=1
    if n==0 or n==1:
        return s
    else:
        return fact(n-1)*n
def sum(a,b):
    return a+b
def Sum(m):
    s=0
    while(m>0):
        s=sum(s,fact(m))
        m=m-1
    return s

print(Sum(10))


def f(x):
    return x*x
def list_prime(l=[]):
    print()
    h=[]
    for i in l:
        s=0
        for j in range(2,i):
            if(i%j==0):
                s+=1
        if s==0:
            h.append(i)
        s=0
        for i in h:
           s+=f(i)
    return h,s
print(list_prime([2,3,5,4,62,56,4]))


def numlist():
    h=[]
    for i in range(1,27):
       h.append(i)
    return h
def charlist():
    h=[]
    j='A'
    for i in range(26):
        h.append(chr(ord(j)+i))
    return h
print(numlist())
print(charlist())
dict=dict(zip(numlist(),charlist()))
for i in dict.keys():
    if i%2==0:
        print(dict[i],end=' ')

import turtle
def kehe(len,n):
    if n==0:
        turtle.fd(len)
    else:
        for i in[0,60,-120,60]:
            turtle.left(i)
            kehe(len/3,n-1)
lenth = 500
level = 5
du = 120
def main():
    turtle.penup()
    turtle.goto(-100,100)
    turtle.pensize(2)
    turtle.color('green')
    turtle.pendown()
    kehe(lenth,level)
    turtle.right(du)
    kehe(lenth, level)
    turtle.right(du)
    kehe(lenth, level)
    turtle.right(du)
    turtle.hideturtle()
    turtle.done()

main()