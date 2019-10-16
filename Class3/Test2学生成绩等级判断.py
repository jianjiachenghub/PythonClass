score=eval(input("输入此学生的成绩"))
grade=""
if score>100 and score<0:
    print("成绩输入出错！请重启程序重新输入！")
elif score<=100 and score>=85:
    grade="A"
elif score<85 and score>=70:
    grade="B"
elif score<70 and score>=60:
    grade="C"
else:
    grade="D"
print("学生成绩等级为{}".format(grade))

