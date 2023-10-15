'''方程为f(x)=x^3-n
迭代式为x=(x^3-n)/3*x^2'''


def Square_root_Newton(n):
    i=n/2
    while(abs(i*i*i-n)>0.00000000001):
        i=i-(i*i*i-n)/(3*i*i)
    return i
print(Square_root_Newton(10))
