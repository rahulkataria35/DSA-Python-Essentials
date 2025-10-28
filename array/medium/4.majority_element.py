"""
Link :> https://www.codingninjas.com/studio/problems/majority-element_6783241?utm_source=striver&utm_medium=website&utm_campaign=codestudio_a_zcourse
LeetCode :> https://leetcode.com/problems/majority-element/
Problem Statement: Given an array of N integers, write a program to return an element that occurs more than N/2 times in the given array. 
You may consider that such an element always exists in the array.

Example
Input Format: N = 3, nums[] = {3,2,3}
Result: 3
Explanation: When we just count the occurrences of each number and compare with half of the size of the array, you will get 3 for the above solution. 

THis Problem uses "Moore's Voting Algorithm"
"""

# given an arr with len = n, you have to find the majority element has length > n/2

# brute-force
# time = O(n^2)
# space = O(1)
def majority_ele(arr):
    n = len(arr)
    
    for i in range(n):
        count = 0
        for j in range(n):
            if arr[i] == arr[j]:
                count += 1
            if count > n/2:
                return arr[i]
    return None

# better_approach
# time = O(2n)
# space = O(n)
def majority_ele_(arr):
    n =len(arr)
    hash_map = {}
    
    for i in range(n):
        if arr[i] in hash_map:
            hash_map[arr[i]] += 1
        else:
            hash_map[arr[i]] = 1
    
    for key, value in hash_map.items():
        if value > n/2:
            return key
    return None
    
    

# best_approach || Moores Voting algorithm
# time = O(n)
# space = O(1)


def majorityElement(arr):
    n = len(arr)
    cnt = 0  # Count
    el = None  # Element

    # Applying the algorithm
    for i in range(n):
        if cnt == 0:
            cnt = 1
            el = arr[i]
        elif el == arr[i]:
            cnt += 1
        else:
            cnt -= 1

    # Checking if the stored element is the majority element
    cnt1 = 0
    for i in range(n):
        if arr[i] == el:
            cnt1 += 1

    if cnt1 > (n / 2):
        return el
    return -1

     
    
arr = [7,7,5,7,5,1,5,7,5,5,7,7,5,5,5,5]
print(majorityElement(arr))