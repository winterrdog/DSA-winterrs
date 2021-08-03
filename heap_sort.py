#!/usr/bin/env python3

"""
    Heaps can be used in sorting an array. In max-heaps, maximum element will always
    be at the root. Heap Sort uses this property of heap to sort the array. In min-heaps, 
    minimum element will always be at the root.

    Consider an array  which is to be sorted using Heap Sort.

    1. Initially build a max heap of elements in ARR.
    2. The root element, that is ARR[1], will contain maximum element of ARR. After that, swap 
       this element with the last element of ARR and heapify the max heap excluding the last 
       element which is already in its correct position and then decrease the length of heap by one.
    3. Repeat the step 2, until all the elements are in their correct position.

    Refer to https://www.geeksforgeeks.org/heap-sort/ for more info on implementation.
"""

# Python program for implementation of heap Sort

# To heapify subtree rooted at index 'root_loc'.
# arr_len is size of heap


def heapify(arr, arr_len, root_loc):
    # NOTE WE'RE DEALING WITH ARRAY INDICES OR REFERENCES OR LOCATIONS INI THIS FN.
    # Initialize largest item(which is always at the top) as root of the binary tree or
    # subtrees --> parent_node
    parent_node_loc = root_loc
    left_node_loc = 2 * root_loc + 1
    right_node_loc = 2 * root_loc + 2

    # See if a left child location of root exists and is greater than root(parent_node)
    if (left_node_loc < arr_len) and (arr[parent_node_loc] < arr[left_node_loc]):
        parent_node_loc = left_node_loc

    # See if right child of root exists and is greater than root
    if (right_node_loc < arr_len) and (arr[parent_node_loc] < arr[right_node_loc]):
        parent_node_loc = right_node_loc

    # Update the root loc when the current parent loc has been changed
    if not (parent_node_loc == root_loc):
        # Swap the root loc for the current parent_loc
        arr[parent_node_loc], arr[root_loc] = (arr[root_loc], arr[parent_node_loc])
        heapify(arr, arr_len, parent_node_loc)  # heapify the root


def heap_sort(arr):
    arr_len = len(arr)

    # Build the initial max heap
    for curr_pos in range((arr_len // 2), -1, -1):
        heapify(arr, arr_len, curr_pos)

    # One by one shift the largest elements to the end. Loop starting with the
    # index
    for curr_index in range((arr_len - 1), 0, -1):
        arr[curr_index], arr[0] = (arr[0], arr[curr_index])
        heapify(arr, curr_index, 0)

    return arr


if __name__ == "__main__":
    alist = [54, 26, 93, 17, 77, 102, 31, 44, 55, 20]
    print(heap_sort(alist))
