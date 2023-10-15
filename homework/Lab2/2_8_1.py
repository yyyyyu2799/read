#蒙特卡洛法求圆周率#
import random
def jihefa():
    x=random.random()
    y=random.random()
    return(x*x+y*y)
count=0
for i in range(1,100000):
    if(jihefa()<=1):
        count+=1
print(round(4*count/100000,10))



#该方法的效率为line8中自行设置的循环次数，本程序中为100000，且不能保证准确率

    
