from typing import List
import inspect


def bubble_sort(nums: List[int]):
    """
    冒泡排序:逐次交换
    时间复杂度O(n^2)
    空间复杂度O(1)
    """
    n = len(nums)

    for i in range(n - 1):
        flag = True
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                flag = False

        if flag:
            break
    format_print(nums)


def insert_sort(array: List[int]):
    """
    插入排序: 构建有序序列，将无序序列的元素依次和有序序列比较
    时间复杂度O(n^2)
    空间复杂度O(1)
    """
    n = len(array)
    for i in range(1, n):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    format_print(array)


def merge_sort(array: List[int]):
    """
    归并排序: 分治法， 看作有序序列合并
    时间复杂度O(nlogn)
    空间复杂度O(n)
    """
    import math

    def iteration(array: List[int]):
        if len(array) <= 1:
            return array

        mid = math.floor(len(array) / 2)
        left = iteration(array[:mid])
        right = iteration(array[mid:])
        return merge(left, right)

    def merge(left: List[int], right: List[int]):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[i]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[i])
                j += 1

        while i < len(left):
            result.append(left[i])
            i += 1

        while j < len(right):
            result.append(right[j])
            j += 1

        return result

    format_print(iteration(array))


def quick_sort(array: List[int]):
    """
    快速排序: 分治法，定位基准，定位所有基准后，即完成排序
    时间复杂度O(logn)
    空间复杂度O(n)
    """

    def sort(arr: List[int]):
        if len(arr) <= 1:
            return arr

        pivot = arr[0]

        left = [x for x in arr[1:] if x <= pivot]  # 需要去掉基准
        right = [x for x in arr[1:] if x > pivot]

        return sort(left) + [pivot] + sort(right)

    format_print(sort(array))


def format_print(array: List[int]):
    caller = inspect.stack()[1].function
    print(f"{caller} -> {array}")


if __name__ == "__main__":
    test = [5, 2, 3, 1, 2, 3, 5]
    bubble_sort(test)
    insert_sort(test)
    merge_sort(test)
    quick_sort(test)
