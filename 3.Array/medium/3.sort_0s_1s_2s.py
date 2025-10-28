'''
Link >> https://www.codingninjas.com/studio/problems/631055?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
Link LeetCode >> https://leetcode.com/problems/sort-colors/
Problem Statement: Given an array consisting of only 0s, 1s, and 2s. 
Write a program to in-place sort the array without using inbuilt sort functions. 

( Expected: Single pass-O(N) and constant space)
Example:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
'''

# time complexity = O(2n), space complexity = O(1)
def sort_arr(arr):
    n = len(arr)
    count0 = count1 = count2 = 0
    
    for i in range(n):
        if arr[i] == 0:
            count0 += 1
        elif arr[i] == 1:
            count1 += 1
        else:
            count2 += 1
    print(count0, count1, count2)
    
    for i in range(count0):
        arr[i] = 0
    for i in range(count0, count0+count1):
        arr[i] = 1  
    for i in range(count0+count1, n):
        arr[i] = 2
    return arr

def sort_arr_(arr):
    counts = [0, 0, 0]
    for num in arr:
        counts[num] += 1
    
    arr[:] = [0] * counts[0] + [1] * counts[1] + [2] * counts[2]
    return arr



# Time Complexity: O(n)
# Space Complexity: O(1)

# Approach 2: Using Dutch National Flag Algorithm
def sort_arr__(arr):
    low = mid = 0
    high = len(arr) - 1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr



arr = [0,1,1,0,0,1,2,2,0,1,2,2,1]
print(sort_arr__(arr))
