#!/usr/bin/env python3


def quick_sort(arr):
    first_index = 0
    last_index = len(arr) - 1

    sorted_arr = quick_sort_recur(arr, first_index, last_index)
    return sorted_arr


def quick_sort_recur(arr, start_index, end_index, msg=''):
    print(f"\nStarting {msg} recursion...")
    print(f"Curr arr: {arr}")
    print(f"Orig Start index: {start_index} :: end index: {end_index}")

    if start_index < end_index:  # Our recursive base case
        pos = partition(arr, start_index, end_index)
        print(f"Curr position: {pos}")

        # Scans looking backwards from the wall('pos' in this case)
        # reason we add/subtract one is avoid changes on the previous pivot but only look
        # after it and before it.
        quick_sort_recur(arr, start_index, (pos - 1), '1st')

        # Scans looking forwards from the wall('pos' in this case)
        quick_sort_recur(arr, (pos + 1), end_index, '2nd')

    return arr


def partition(arr, start_index, end_index):
    wall = start_index  # wall is a variable to mark the recent pivot
    print(f"Curr wall: {wall}")
    print(f"partition func: start_index: {start_index} :: end_index:{end_index}")

    # For loop to traverse the whole array sorting items less than the pivot to its
    # left and those greater to its right.
    for pos in range(start_index, end_index):
        if arr[pos] < arr[end_index]:  # end_index is the pivot
            arr[pos], arr[wall] = (arr[wall], arr[pos])
            print(f"'partition for loop' Curr pos: {pos} :: Curr wall: {wall}")
            wall += 1

    # swapping the old pivot for the new pivot(which goes to the end)
    arr[wall], arr[end_index] = (arr[end_index], arr[wall])
    return wall


if __name__ == "__main__":
    alist = [54, 26, 93, 17, 77, 102, 31, 44, 55, 20]
    print(quick_sort(alist))
