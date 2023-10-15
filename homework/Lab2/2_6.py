def Square_root_Newton1(n):#g=c/2
    i=n/2
    while(abs(i*i-n)>0.00000000001):
        i=i-(i*i-n)/(2*i)
    return i
def Square_root_Newton2(n):#g=c
    j=n
    while(abs(j*j-n)>0.00000000001):
        j=j-(j*j-n)/(2*j)
    return j
def Square_root_Newton3(n):#g=c/4
    k=n/4
    while(abs(k*k-n)>0.00000000001):
        k=k-(k*k-n)/(2*k)
    return k
print(Square_root_Newton1(2))
print(Square_root_Newton2(2))
print(Square_root_Newton3(2))
print(Square_root_Newton1(2000))
print(Square_root_Newton2(2000))
print(Square_root_Newton3(2000))


#通过观察，发现起始值对结果有影响
'''
求解根号2,初始值分别设为g=c g=c/2 g=c/4 所得结果如下
1.4142135623746899
1.4142135623746899
1.4142135623730951
'''