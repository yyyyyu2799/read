#pi/4级数展开为1-1/3+1/5-1/7...#
import math
k=0
j=0
while 1:
    k+=(-1)**j/(2*j+1)
    j+=1
    if(abs(4*k-math.pi)<0.000000001):
        break
print(round(4*k,10))
print(j)
#该方法效率较低，精度达到小数点后9位的效率为998280591，精度达到十位的结果运行时间太长
