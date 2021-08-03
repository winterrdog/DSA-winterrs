#!/usr/bin/env python3
"""
https://en.wikipedia.org/wiki/Bubble_sort

    ** Worst-case performance: O(N^2) **
    If you call bubble_sort(arr), you can see the process of the sort

    Bubble sort is based on the idea of repeatedly comparing pairs of adjacent elements 
    and then swapping their positions if they exist in the wrong order
"""


def bubble_sort(arr):
    def swap(i, j):
        arr[i], arr[j] = (arr[j], arr[i])

    arr_len = len(arr)
    keep_swapping = True

    x = -1
    while keep_swapping:
        keep_swapping = False
        x += 1
        for i in range(1, (arr_len - x)):
            if arr[i - 1] > arr[i]:  # Compare elements
                swap((i - 1), i)
                keep_swapping = True

    return arr


if __name__ == "__main__":
    alist = [54, 26, 93, 17, 77, 102, 31, 44, 55, 20]
    print(bubble_sort(alist))
