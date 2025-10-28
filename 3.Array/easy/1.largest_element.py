'''
Problem statement
Given an array 'arr' of size 'n' find the largest element in the array.

Example:
Input: 'n' = 5, 'arr' = [1, 2, 3, 4, 5]
Output: 5
Explanation: From the array {1, 2, 3, 4, 5}, the largest element is 5.
'''

# time: O(NlogN)
def largest(arr):
    arr.sort()
    return arr[-1]

# Time Complexity: O(N)
# Space Complexity: O(1)

# find lasrgest element
def largest_ele(arr):
    n = len(arr)

    if n ==1:
        return arr[0]
    
    maximum = arr[0]
    for ele in range(1, n):
        if arr[ele] > maximum:
            maximum = arr[ele]
    return maximum

arr = [1,3,5,2,8,4]
print(largest_ele(arr))

