#!/usr/bin/env python3
"""
    Insertion sort is based on the idea that one element from the input elements is
    consumed in each iteration to find its correct position i.e, the position to which
    it belongs in a sorted array.
"""


def insertion_sort(arr):
    """
    Insertion Sort
    Complexity: O(n^2)
    """

    def swap(i, j):
        arr[i], arr[j] = (arr[j], arr[i])

    # Scan the entire array doing the insertion sort
    for arr_ptr in range(len(arr)):
        curr_pos = arr_ptr

        # Keep swapping values that are greater than the current item and later save the
        # position where the swapping occurred
        while (curr_pos > 0) and (arr[curr_pos - 1] > arr[curr_pos]):
            # Swap the current item down the list
            swap(curr_pos - 1, curr_pos)
            curr_pos -= 1  # Reduce the current position.

    return arr


if __name__ == "__main__":
    alist = [54, 26, 93, 17, 17, 77, 102, 54, 31, 44, 55, 20]
    print(insertion_sort(alist))
