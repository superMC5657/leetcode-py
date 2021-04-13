# -*- coding: utf-8 -*-
# !@time: 2021/4/13 下午2:22
# !@author: superMC @email: 18758266469@163.com
# !@fileName: quick_sort.py


def quick_sort(array, left, right):
    if left >= right:
        return array
    pivot, i, j = array[left], left, right
    while i < j:
        while i < j and array[j] >= pivot:
            j -= 1
        array[i] = array[j]
        while i < j and array[i] <= pivot:
            i += 1
        array[j] = array[i]
    array[j] = pivot
    quick_sort(array, left, i - 1)
    quick_sort(array, i + 1, right)
    return array


array = [1, 2, 4, 6, 3, 4, 5, 7, 9, 1]
ret = quick_sort(array, 0, len(array)-1)
print(ret)
