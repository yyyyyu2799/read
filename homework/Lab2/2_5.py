def Square_root_Newton(n):
    i=n/2
    while(abs(i*i-n)>0.00000000001):
        i=i-(i*i-n)/(2*i)
    return i
print(Square_root_Newton(2))
print(Square_root_Newton(2000))