'''（1）667个3

    (2)将n分成若干个相等的正整数之和，它们的乘积最大的情况是将n分成若干个3和2的和。
       这是因为对于一个大于等于5的正整数，将其分成3和2的和可以得到更大的乘积。
       具体来说，如果n除以3余数为0，则将n分成n/3个3；如果余数为1，则将n分成(n-4)/3个3和2个2；
                如果余数为2，则将n分成(n-2)/3个3和1个2。
       先把n<=2的情况罗列出来，然后再计算n>=5时的情况
       处理n>=5时，先求n%3，根据余数的值，按照上述描述分类




'''

def maxProduct(n):
    if (n<=0):
        return False
    elif ( n==1):
        print(0)
        print(1)
        return 0
    elif (n==2):
        print(1)
        print(1)
        return 0
    elif(n==3):
        print(1)
        print(2)
        return 0
    elif(n==4):
        print(2)
        print(2)
        return 0
    else:
        if(n%3==0):
            return int(n/3)
        elif(n%3==1):
            print(2)
            print(2)
            return int((n-4)/3)
        else:
            print(2)
            return int((n-2)/3)
n=2001
k=maxProduct(n)
for i in range(0,k):
    print(3)



            

    
    
    






