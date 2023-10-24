#思考如何利用 Python 获取程序执行时间并实现
#利用time包
import time
def test():
    start_time = time.time()  # 记录程序开始运行时间
    s = 0
    for i in range(1000000):
        s += 1
    end_time = time.time()  # 记录程序结束运行时间
    print('cost %f second' % (end_time - start_time))
    return s
s=test()
print(s)
