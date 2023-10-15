import random
import math
def jihefa():
    x=random.uniform(2,3)
    y=random.uniform(0,21)
    return(y-x*x-4*x*math.sin(x))
count=0
for i in range(1,10000000000):
    if(jihefa()<=0):
        count+=1
print(round(21*count/10000000000,2))


