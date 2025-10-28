'''
Given an array of integers nums and an integer target, return indices of the two numbers such that 
they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element 
twice.

You can return the answer in any order. 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
'''



# brute force--> time complexity = O(n^2) and space-complexity = O(1)
def two_sum(arr, target):
    n = len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] + arr[j] == target:
                return [i,j]  # or we can return "YES"
    return None


# better solution --> using hashing time(n) and space = O(n)
def two_sum_(arr, target):
    hash_map = {}
    n = len(arr)
    for i in range(n):
        if target - arr[i] in hash_map:
            return [hash_map[target-arr[i]], i]
        hash_map[arr[i]] = i
    return None


######################### BEST solution for YES/NO ##############################
# one more better solution for variety one probelem : like just return "yes" or "no"
# time = O(nlogn), space = O(1)
def two_sum__(arr, target):
    arr.sort()
    i = 0
    j = len(arr)-1
    
    while i < j:
        res = arr[i] + arr[j]
        if res == target:
            return "Yes"
        if res < target:
            i += 1
        else:
            j -= 1
    return "No"



        


arr = [2,6,5,8,11]
target = 14

print(two_sum__(arr,target))
    