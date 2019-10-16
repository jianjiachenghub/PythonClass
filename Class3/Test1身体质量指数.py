weight=eval(input("输入体重(KG)："))
height=eval(input("输入身高(M)："))
bmi=weight/pow(height,2)
print("BMI数值为：{:.2f}".format(bmi))
who,dom="",""
if bmi<18.5:
    who="偏瘦"
elif bmi>=18.5 and bmi<25:
    who="正常"
elif bmi>=25 and bmi<30:
    who="偏胖"
else:
    dom="肥胖"
if bmi<18.5:
    dom="偏瘦"
elif bmi>=18.5 and bmi<24:
    dom="正常"
elif bmi>=24 and bmi<28:
    dom="偏胖"
else:
    dom="肥胖"
print("BMI指标为：国际'{0}',国内'{1}'".format(who,dom))

