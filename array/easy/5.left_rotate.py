
# left rotate arr by one place
# Time complexity: O(n)
# - Slicing the array and concatenating it takes O(n) time, where n is the length of the array.

# Space complexity: O(n)
# - The operation creates a new array of the same size as the input array, so it takes O(n) space.
def left_rotate_by_one(arr):
    return arr[1:]+ [arr[0]]



'''
Time Complexity: O(n), as we iterate through the array only once.

Space Complexity: O(n) as we are using another array of size, same as the given array.
'''

def left_rotate_by_one_1(arr):
    n = len(arr)
    temp_arr = [0]*n

    for i in range(1, n):
        temp_arr[i-1] = arr[i]
    temp_arr[n-1] = arr[0]
    return temp_arr


'''
Time Complexity: O(n), as we iterate through the array only once.

Space Complexity: O(1) as no extra space is used
'''

def left_rotate_by_one_2(arr):
    first_val = arr[0]
    n = len(arr)

    for i in range(n-1):
        arr[i] = arr[i+1]
    arr[n-1] = first_val
    return arr

arr = [1,2,3,4]

# print(left_rotate_by_one_2(arr))


#_______________________________left rotate by d-places___________________________

def left_rotate_by_d_places(arr,d):
    return arr[d:]+ arr[:d]





# Time complexity: O(n)
# - The loop runs n times, where n is the length of the array.
# - Each assignment operation inside the loop takes O(1) time.
# - Overall, the time complexity is O(n).

# Space complexity: O(n)
# - The temporary array `temp_arr` is of the same size as the input array.
# - Therefore, the space complexity is O(n).
def left_rotate_by_d_places_1(arr,d):
    n = len(arr)
    d = d%n
    temp_arr = [0]*n
    for i in range(d, n):
        temp_arr[i-d] = arr[i]
    for i in range(d):
        temp_arr[n-d+i] = arr[i]
    return temp_arr

arr = [1,2,3,4,5,6,7,8]
# print(left_rotate_by_d_places_1(arr,2))



# best solution
def left_rot_by_d(arr, d):
    n = len(arr)
    d = d%n
    for i in range(d, n):
        arr[i-d], arr[i] = arr[i], arr[i-d]
    return arr


def left_rotate_by_d(arr,d):
    n = len(arr)
    temp = arr[:d]
    
    for i in range(d, n):
        arr[i-d] = arr[i]
    
    for i in range(d):
        arr[n-d+i] = temp[i]
    return arr

# print(left_rotate_by_d(arr,3))

# most optimimal approach is

def reverse_array(arr, start, end):
    """
    Reverse a portion of the array in-place.
    """
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def left_rotate_array(arr, d):
    """
    Rotate the array to the left by d places.
    """
    n = len(arr)
    d = d % n  # handle cases where d > n
    reverse_array(arr, 0, d - 1)
    reverse_array(arr, d, n - 1)
    reverse_array(arr, 0, n - 1)
    return arr

# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # example array
print(left_rotate_array(arr, 3))


