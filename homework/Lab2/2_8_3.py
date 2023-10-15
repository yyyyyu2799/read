#2/pi=cos(pi/4)*cos(pi/8)*cos(pi/16)*cos(pi/32)*...
import math
i=2
res=1
while 1:
    res*=math.cos(math.pi/(2**i))
    i+=1
    if(abs(2/res-math.pi)<0.0000000001):
        break
        
print(round(2/res,10))
print(i)
#效率为19