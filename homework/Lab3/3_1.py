
#小数部分的转化
def decimal_to_binary(decimal, num_of_digits=5):
    binary = ""
    for _ in range(num_of_digits):
        decimal *= 2
        digit = int(decimal)
        binary += str(digit)
        decimal -= digit
    return binary



#整数部分的转化
num=float(input("请输入十进制小数:"))
n=int(num)
binary_number = bin(n)


decimal = num-n
binary = decimal_to_binary(decimal)
print(binary_number+"."+binary)







