def linear_search(arr, num):
    for i in range(len(arr)):
        if arr[i] == num:
            return i
    return -1
