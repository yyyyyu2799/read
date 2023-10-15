#首先，我们可以构建两个辅助数组C和D，其中C[i]表示AxAx…xA[i-1]，D[i]表示A[i+1]xA[i+2]x…xA[n-1]。
#然后，我们可以根据C和D数组构建B数组，B[i]=C[i]xD[i]。
def construct_array(A):
    n = len(A)
    C = [1] * n
    D = [1] * n
    B = [1] * n

    # 计算C数组
    for i in range(1, n):
        C[i] = C[i-1] * A[i-1]

    # 计算D数组
    for i in range(n-2, -1, -1):
        D[i] = D[i+1] * A[i+1]

    # 构建B数组
    for i in range(n):
        B[i] = C[i] * D[i]

    return B

A = [1, 2, 3, 4, 5]
print(construct_array(A))  # 输出 [120, 60, 40, 30, 24]