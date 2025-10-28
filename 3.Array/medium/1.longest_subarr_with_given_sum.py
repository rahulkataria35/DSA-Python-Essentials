
'''
Link :> https://www.codingninjas.com/studio/problems/longest-subarray-with-sum-k_6682399?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_Arrayproblems
Problem Statement: Given an array and a sum k, we need to print the length of the longest subarray that sums to k.
Example :
Input Format: N = 3, k = 5, array[] = {2,3,5}
Result: 2
Explanation: The longest subarray with sum 5 is {2, 3}. And its length is 2.
Sliding Window Technique Question >> That to of variable window 
Because  the lenght of window is not defined but the sum of the window should be of K which is given. 
'''

'''
find the longest subarray with given sum (positive)
'''
arr = [1,2,1,4,2,1,1,1,1,4,6,3]
k = 3


# time complexity ~ O(n^3) and space_complexity = O(1)
def find_subarr_sum_k(arr,k):
    n = len(arr)
    max_len = 0
    
    for i in range(n):
        for j in range(i, n):
            summ = 0
            for idx in range(i,j+1):
                summ += arr[idx]
            if summ == k:
                max_len = max(max_len, j-i+1)
    return max_len


# time complexity ~ O(n^2) and space_complexity = O(1)
def find_subarr_sum_k_(arr,k):
    n = len(arr)
    max_len = 0
    
    for i in range(n):
        summ = 0
        for j in range(i, n):   
            summ += arr[j]
            if summ == k:
                max_len = max(max_len, j-i+1)
    return max_len

        
# same as above
'''
Time Complexity: O(N) or O(N*logN) depending on which map data structure we are using, where N = size of the array.
Reason: For example, if we are using an unordered_map data structure in C++ the time complexity will be O(N)(though 
in the worst case, unordered_map takes O(N) to find an element and the time complexity becomes O(N2)) but if we are
using a map data structure, the time complexity will be O(N*logN). The least complexity will be O(N) as we are using
a loop to traverse the array.

Space Complexity: O(N) as we are using a map data structure.
'''

# this approach is work for +ve, -ves and zeros
def find_subarr_sum_k__(a, k):
    n = len(a) # size of the array.
    preSumMap = {}
    Sum = 0
    maxLen = 0
    
    for i in range(n):
        # calculate the prefix sum till index i:
        Sum += a[i]

        # if the sum = k, update the maxLen:
        if Sum == k:
            maxLen = max(maxLen, i + 1)

        # calculate the sum of remaining part i.e. x-k:
        rem = Sum - k

        # Calculate the length and update maxLen:
        if rem in preSumMap:
            length = i - preSumMap[rem]
            maxLen = max(maxLen, length)

        # Finally, update the map checking the conditions: it handles the case when we have zeros in the array for eg: arr = [2,0,0,3], k = 3
        if Sum not in preSumMap:
            preSumMap[Sum] = i

    return maxLen        
    
    
# this optimal approach is only work for +ves and zeros, not for -ves        
def getLongestSubarray(a, k):
    n = len(a) # size of the array.

    left, right = 0, 0 # 2 pointers
    Sum = a[0]
    maxLen = 0
    while right < n:
        # if sum > k, reduce the subarray from left
        # until sum becomes less or equal to k:
        while left <= right and Sum > k:
            Sum -= a[left]
            left += 1

        # if sum = k, update the maxLen i.e. answer:
        if Sum == k:
            maxLen = max(maxLen, right - left + 1)

        # Move forward the right pointer:
        right += 1
        if right < n: Sum += a[right]

    return maxLen
'''
Time Complexity: O(2*N), where N = size of the given array.
Reason: The outer while loop i.e. the right pointer can move up to index n-1(the last index). Now, the inner while loop 
i.e. the left pointer can move up to the right pointer at most. So, every time the inner loop does not run for n times 
rather it can run for n times in total. So, the time complexity will be O(2*N) instead of O(N2).

Space Complexity: O(1) as we are not using any extra space.
'''

print(find_subarr_sum_k__(arr, k))
                
            
            