import random
import time

# 生成随机数列
def generate_random_list(length):
    return [random.randint(0, 1000) for _ in range(length)]

# 选择排序
def selection_sort(lst):
    for i in range(len(lst)):
        min_index = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]

# 归并排序
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

# 测试排序算法的运行时间
def test_sorting_algorithm(algorithm, lst):
    start_time = time.time()
    algorithm(lst)
    end_time = time.time()
    return end_time - start_time

# 测试
for i in range(5):
    length = (i+1) * 1000
    lst = generate_random_list(length)
    print(f"数列长度: {length}")
    print(f"选择排序: {test_sorting_algorithm(selection_sort, lst)}","秒")
    print(f"归并排序: {test_sorting_algorithm(merge_sort, lst)}","秒")
    print("=====================")