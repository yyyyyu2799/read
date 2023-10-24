#编写 Python 程序,判断输入 a 是否为质数
import math
a=int(input("请输入整数a:"))
sqrt_a=int(math.sqrt(a))
flag=0
for i in range(2,sqrt_a+1):
    if(a%i==0):
        flag=1
        break
if(flag==1):
    print("a不是质数")
else:
    print("a是质数")

