def jiecheng(n):
    if(n==0):
        return 1
    else:
        result=n
        while n-1>0:
            result*=(n-1)
            n=n-1
        return result
n=int(input("请输入n:"))
print(jiecheng(n))