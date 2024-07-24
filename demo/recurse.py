import os

root_dir = r"site"


def search_all_files(dir_path: str):
    """
    搜索目录下所有文件
    """
    for file_name in os.listdir(dir_path):
        file_path = os.path.join(dir_path, file_name)
        if os.path.isdir(file_path):  # 递归步骤是继续遍历目录
            search_all_files(file_path)
        else:  # file: 基线条件是文件
            print(file_path)


search_all_files(root_dir)


"""
递归实现快速排序
"""


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]  # 分界点
        left = [i for i in arr[1:] if i <= pivot]
        right = [i for i in arr[1:] if i > pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)


def bubble_sort(arr):
    n = len(arr)
    result = list(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
    return result


arr = [5, 2, 8, 3, 9, 1]
print(quick_sort(arr))
print(bubble_sort(arr))

"""
递归实现斐波那契数列
"""


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_memory(n, memo: dict = None) -> int:
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    else:
        memo[n] = fibonacci_memory(n - 1, memo) + fibonacci_memory(n - 2, memo)
        return memo[n]


print(fibonacci(10))
print(fibonacci_memory(10))
