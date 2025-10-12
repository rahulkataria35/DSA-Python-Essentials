
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