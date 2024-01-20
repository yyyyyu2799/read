
w=int(input("请输入w:"))
x=int(input("请输入x:"))
y=int(input("请输入y:"))
z=int(input("请输入z:"))
if(x<w):
    t=x
    x=w
    w=t
if(y<=x and y>=w):
    t=x
    x=y
    y=t
if(y<=w):
    t=x
    x=y
    y=t
    t=x
    x=w
    w=t
if(z>=x and z<=y):
    t=y
    y=z
    z=t
if(z>=w and z<=x):
    t=y
    y=z
    z=t
    t=x
    x=y
    y=t
if(z<=w):
    t=y
    y=z
    z=t
    t=x
    x=y
    y=t
    t=x
    x=w
    w=t

print(w,x,y,z)


    


