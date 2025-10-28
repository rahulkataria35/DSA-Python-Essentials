'''
Link: https://www.codingninjas.com/studio/problems/traffic_6682625?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
Problem Statement: Given an array that contains only 1 and 0 return the count of maximum consecutive ones in the array.
Example :
Input: prices = {1, 1, 0, 1, 1, 1}
Output: 3
Explanation: There are two consecutive 1's and three consecutive 1's in the array out of which maximum is 3.

'''

arr = [1,1,0,0,0,1,1,1,0,0,1,0,1,1]

# output should be 3

def find_max_consecutive_ones(arr):
    """
    Find the maximum number of consecutive ones in the array.
    """
    max_ones = 0
    current_ones = 0
    for num in arr:
        if num == 1:
            current_ones += 1
            max_ones = max(max_ones, current_ones)
        else:
            current_ones = 0
    return max_ones
    
print(find_max_consecutive_ones(arr))