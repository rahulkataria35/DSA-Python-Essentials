arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # example array
# output = [9, 1, 2, 3, 4, 5, 6, 7, 8]

def right_rotate_by_one(arr):
    if not arr:
        return []
    return [arr[-1]] + arr[:-1]



def right_rotate_by_one_1(arr):
    if not arr:
        return []
    
    n = len(arr)
    temp = arr[-1]
    
    for i in range(n-1, 0, -1):
        arr[i] = arr[i-1]
        
    arr[0] = temp
    return arr

# print(right_rotate_by_one_1(arr))

###############################################################



def right_rotate_by_d_places(arr, d):
    n = len(arr)
    d = d%n
    
    temp = arr[n-d:]
    temp_arr = [0]*n
    
    for i in range(0, n-d):
        temp_arr[i+d] = arr[i]
    
    for i in range(d):
        temp_arr[i] = temp[i]
    return temp_arr



def reverse_array(arr, start, end):
    """
    Reverse a portion of the array in-place.
    """
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def right_rotate(arr, d):
    n = len(arr)
    d = d%n
    
    reverse_array(arr, 0, n-d-1)
    reverse_array(arr, n-d, n-1)
    reverse_array(arr, 0,n-1)
    return arr

print(right_rotate(arr, 3))
    