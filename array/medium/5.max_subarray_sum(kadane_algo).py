'''
Kadane's Algorithm is used to find the maximum sum of a contiguous subarray in a given
array of integers. Here's a Python implementation of the algorithm:
'''

def kadane_algorithm(arr):
    max_so_far = arr[0]
    max_ending_here = arr[0]

    for i in range(1, len(arr)):
        max_ending_here = max(arr[i], max_ending_here + arr[i])
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far

# Example usage
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Maximum contiguous sum is", kadane_algorithm(arr))



# 
def kadane_algorithm_detail(arr):
    max_so_far = arr[0]
    max_ending_here = arr[0]
    
    start = end = s = 0

    for i in range(1, len(arr)):
        if arr[i] > max_ending_here + arr[i]:
            max_ending_here = arr[i]
            s = i
        else:
            max_ending_here += arr[i]
        
        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
            start = s
            end = i

    return max_so_far, arr[start:end + 1]


    

# Example usage
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum, subarray = kadane_algorithm_detail(arr)
print("Maximum contiguous sum is", max_sum)
print("Subarray with the maximum sum is", subarray)
