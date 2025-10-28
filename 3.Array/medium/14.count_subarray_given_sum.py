'''
Coding Ninja :> https://www.codingninjas.com/studio/problems/subarray-sums-i_1467103?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
LeetCode :> https://leetcode.com/problems/subarray-sum-equals-k/description/

Problem Statement: Given an array of integers and an integer k, return the total number of subarrays whose sum equals k.
A subarray is a contiguous non-empty sequence of elements within an array.
Example :
Input Format: N = 4, array[] = {3, 1, 2, 4}, k = 6
Result: 2
Explanation: The subarrays that sum up to 6 are [3, 1, 2] and [2, 4].

'''

# brute force approach
# Time Complexity: O(N3),
# spcae = O(1)

def findAllSubarraysWithGivenSum(arr, k):
    n = len(arr)  # size of the given array.
    cnt = 0  # Number of subarrays.

    for i in range(n):  # starting index i.
        for j in range(i, n):  # ending index j.
            # calculate the sum of subarray [i...j].
            subarray_sum = sum(arr[i:j+1])

            # Increase the count if sum == k.
            if subarray_sum == k:
                cnt += 1

    return cnt


###################################3
# Time Complexity: O(N2)
# Space Complexity: O(1)
def findAllSubarraysWithGivenSum(arr, k):
    n = len(arr)  # size of the given array.
    cnt = 0  # Number of subarrays.

    for i in range(n):  # starting index i.
        subarray_sum = 0
        for j in range(i, n):  # ending index j.
            # calculate the sum of subarray [i...j]
            # sum of [i..j-1] + arr[j]
            subarray_sum += arr[j]

            # Increase the count if sum == k.
            if subarray_sum == k:
                cnt += 1

    return cnt


##########################################

from collections import defaultdict

def findAllSubarraysWithGivenSum(arr, k):
    n = len(arr) # size of the given array.
    mpp = defaultdict(int)
    preSum = 0
    cnt = 0

    mpp[0] = 1 # Setting 0 in the map.
    for i in range(n):
        # add current element to prefix Sum:
        preSum += arr[i]

        # Calculate x-k:
        remove = preSum - k

        # Add the number of subarrays to be removed:
        cnt += mpp[remove]

        # Update the count of prefix sum
        # in the map.
        mpp[preSum] += 1

    return cnt


if __name__ == '__main__':
    arr = [3, 1, 2, 4]
    k = 6
    cnt = findAllSubarraysWithGivenSum(arr, k)
    print("The number of subarrays is:", cnt)
