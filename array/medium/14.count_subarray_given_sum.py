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




arr = [1,2,3,-3, 1,1,1,4,2,-3]
k = 3

print(number_of_subarr(arr,k))