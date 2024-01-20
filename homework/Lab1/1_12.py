def cube_root(n):
    x = n / 3  # 初始猜测值
    while True:
        new_x = (2 * x + n / (x ** 2)) / 3
        if abs(new_x - x) < 1e-6:  # 判断迭代是否收敛
            return new_x
        x = new_x
num=int(input())
print(cube_root(num))