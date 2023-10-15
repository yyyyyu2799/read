#辗转相除法求最大公约数
def yueshu(x,y):
    if(x<y):
        t=x
        x=y
        y=t
    temp=x%y
    if(temp==0):
        return y
    else:
        x=y
        y=temp
        return yueshu(x,y)


x=int(input("请输入第一个数:"))
y=int(input("请输入第二个数:"))
print(yueshu(x,y))
