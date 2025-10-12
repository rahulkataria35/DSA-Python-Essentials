# time complexity: O(nlogn)
# space complexity: O(1)
def second_largest(arr):
    arr.sort()
    return arr[-2]


'''
Time Complexity: O(N), We do two linear traversals in our array

Space Complexity: O(1)
'''

def second_largest_2(arr):
    n = len(arr)
    small = float('inf')
    second_small = float("inf")
    largest = float("-inf")
    second_largest = float("-inf")

    for i in range(n):
        small = min(small, arr[i])
        largest = max(largest, arr[i])
    
    for i in range(n):
        if arr[i] < second_small and arr[i] != small:
            second_small = arr[i]
        if arr[i] > second_largest and arr[i] != largest:
            second_largest = arr[i]

    return second_largest


'''
Time Complexity: O(N), Single-pass solution

Space Complexity: O(1)
'''
def second_largest_3(arr):
    largest = float("-inf")
    second_largest = float("-inf")
    n = len(arr)

    for i in range(n):
        if arr[i] > largest:
            second_largest = largest
            largest = arr[i]
        elif arr[i] > second_largest and arr[i] != largest:
            second_largest = arr[i]
    return second_largest

def second_smallest(arr):
    small = float("inf")
    second_small = float("inf")
    n = len(arr)

    for i in range(n):
        if arr[i] < small:
            second_small = small
            small = arr[i]
        elif arr[i] < second_small and arr[i] != small:
            second_small = arr[i]
    
    return second_small


arr = [1,4,5,2,7,9,3,8]
print(second_smallest(arr))




# find 3rd largest
def find_third_largest(arr):
    n = len(arr)
    lar = float("-inf")
    sec_lar = float("-inf")
    third_lar = float("-inf")
    
    for i in range(n):
        if arr[i] > lar:
            third_lar = sec_lar
            sec_lar = lar
            lar = arr[i]
        elif arr[i] > sec_lar and arr[i] != lar:
            third_lar = sec_lar
            sec_lar = arr[i]
        elif arr[i] > third_lar and arr[i] != lar and arr[i] != sec_lar:
            third_lar = arr[i]
   
    return third_lar
            


