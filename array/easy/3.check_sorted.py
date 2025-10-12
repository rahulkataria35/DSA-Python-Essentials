'''
Time Complexity: O(N^2)

Space Complexity: O(1)
'''
def check_sorted_1(arr):
    n = len(arr)

    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                return False

    return True


'''
Time Complexity: O(NlogN)

Space Complexity: O(N)
'''
def check_sorted_2(arr):
    sorted_arr = sorted(arr)
    return sorted_arr == arr


'''
Time Complexity: O(N)

Space Complexity: O(1)
'''
def is_sorted(arr):
    n = len(arr)

    for i in range(1, n):
        if arr[i] < arr[i-1]:
            return False
    return True


arr = [1,2,3,4,5]

# print(is_sorted(arr))


# check arr is sorted in decending  order or ascending order

def is_sorted_4(arr):
    n = len(arr)
    if n <= 1:
        return True  # Empty or single-element arrays are sorted
    
    ascending_order = True
    descending_order = True
    
    for i in range(n - 1):  # Loop till n-2, so arr[i+1] is valid
        if arr[i] > arr[i + 1]:
            ascending_order = False
        if arr[i] < arr[i + 1]:
            descending_order = False
        
        # If both are False, no need to continue
        if not ascending_order and not descending_order:
            return False
    
    return ascending_order or descending_order

print(is_sorted_4(arr))