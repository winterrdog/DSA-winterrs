#!/usr/bin/env python3

"""
    merge_sort STYLE 1
    Merge sort does the following:
    1) recursively dividing the collection, 
    2) sorting it, and 
    3) merging it all back together.
"""


def merge_sort(arr):
    """Merge Sort
    Complexity: O(n log(n))
    """
    # Recursion FIRST FILLS THE CALL STACK from this point
    # Our recursive base case
    if len(arr) <= 1:
        return arr

    mid_point = len(arr) // 2

    # Perform merge_sort recursively on both halves
    left_half = merge_sort(arr[:mid_point])
    right_half = merge_sort(arr[mid_point:])
    #####################################

    # Recursion SECONDLY UNWINDS FROM THE CALL STACK(pops items off the stack till the global context) from this point
    # Merge each side together
    return merge(left_half, right_half, arr.copy())


def merge(left, right, merged):
    """Merge helper
    Complexity: O(n)
    """
    print(f"\nCurr arr: {merged}")
    print(f"left arr: {left} :: right arr: {right}")
    left_cursor, right_cursor = (0, 0)

    # Loop for swapping values
    while left_cursor < len(left) and right_cursor < len(right):
        # Sort each one and place into the result
        if left[left_cursor] <= right[right_cursor]:
            print(f"{left} LEFT array: left_cursor > {left_cursor}")
            merged[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            print(f"{right} RIGHT array: right_cursor > {right_cursor}")
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1

    print(f"[+] after 'while loop': {merged}")
    # Loops to ensure correct replacing and reorder of elements.
    # Add the left overs if there's any left to the result
    for left_cursor in range(left_cursor, len(left)):
        print(
            f"[+] In 'for loop' for left array: {merged[left_cursor + right_cursor]}"
            f" replaced with {left[left_cursor]}"
        )
        merged[left_cursor + right_cursor] = left[left_cursor]

    # Add the left overs if there's any left to the result
    for right_cursor in range(right_cursor, len(right)):
        print(
            f"[+] In 'for loop' for right array: {merged[left_cursor + right_cursor]}"
            f" replaced with {right[right_cursor]}"
        )
        merged[left_cursor + right_cursor] = right[right_cursor]

    print(f"[+] after 'for loop': {merged}")

    # Return result
    return merged


if __name__ == "__main__":
    alist = [54, 26, 93, 17, 77, 102, 31, 44, 55, 20]
    print(merge_sort(alist))
