x=int(input("请输入x:"))
y=int(input("请输入y:"))
z=int(input("请输入z:"))
if(y<x):
    t=x
    x=y
    y=t
if(z>=y):
    print(x,y,z)

elif(z>=x):
    print(x,z,y)
else:
    print(z,x,y)
