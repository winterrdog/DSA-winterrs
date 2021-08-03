#!/usr/bin/env python3
"""
    The Selection sort algorithm is based on the idea of finding the minimum or maximum
    element in an unsorted array and then putting it in its correct position in a sorted array.
"""


def selection_sort(arr):
    """
    Selection Sort
    Complexity: O(n^2)
    """

    def swap(i, j):
        arr[i], arr[j] = (arr[j], arr[i])

    for curr_arr_ptr in range(len(arr)):
        min_item_loc = curr_arr_ptr

        for next_item_loc in range((curr_arr_ptr + 1), len(arr)):
            # "Select" the correct value
            if arr[next_item_loc] < arr[min_item_loc]:
                # Marks the index where the min item is seen
                min_item_loc = next_item_loc

        # Swapping the minimum item into the correct position in the array
        swap(min_item_loc, curr_arr_ptr)

    return arr


if __name__ == "__main__":
    alist = [54, 26, 93, 17, 77, 102, 31, 44, 55, 20]
    print(selection_sort(alist))
