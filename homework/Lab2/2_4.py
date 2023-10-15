def Square_root(n):
    for i in range(0,n):
        if(i*i<=n and (i+1)*(i+1)>n):
            break
    while(abs(i*i-n)>0.0001):
        i+=0.00001
    return i
print(Square_root(2))        
        
