#!/usr/bin/env python3
"""
ref: https://www.tutorialspoint.com/data_structures_algorithms/shell_sort_algorithm.htm

    Shellsort starts by sorting pairs of elements far apart from each other('interval' apart), 
    then progressively reducing the gap between elements to be compared. By starting with far
    apart elements, it can move some out-of-place elements into position faster than a simple
    nearest neighbor exchange.
"""


def shell_sort(arr):
    '''
    Shell Sort
    Complexity: O(n^(3/2))
    '''
    arr_len = len(arr)

    def swap(i, j):
        arr[i], arr[j] = (arr[j], arr[i])

    # Calculate interval using Knuth's formula, h = h*3+1
    interval = 1
    while interval < arr_len // 3:
        interval = interval * 3 + 1

    while interval >= 1:
        for outer in range(interval, arr_len):
            # Select the value to be inserted
            inner = outer

            # Shift element towards right and moving down left the array, "interval"
            # times the array.
            while inner > (interval - 1) and arr[inner - interval] >= arr[inner]:
                # (inner - interval) means the preceding value, "interval" times back(
                # just like saying '2 times back')
                swap(inner, (inner - interval))

                # Move down the sublist interval times.
                inner -= interval

        # Calculate interval
        interval = (interval - 1) // 3

    return arr


if __name__ == "__main__":
    alist = [54, 26, 93, 17, 77, 102, 31, 31, 44, 55, 20]
    print(shell_sort(alist))
