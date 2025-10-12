
'''
find the missing number in an array:

eg: N = 5
ar = [1,2,4,5]

output = 3 is the missing number

'''
    
N = 5
arr = [1,2,4,5]


# brute force--> Time complexity = O(n^2)
def find_missing_number(arr, N):
    for i in range(1,N):
        flag = 0
        for j in range(0, N-1):
            if arr[j] == i:
                flag = 1
                break
        if flag == 0 :
            return i



# time complexity = O(2n) and space complexity = O(n)
def find_missing_num_2(arr, n):
    # Initialize a boolean array to keep track of which numbers are present in the input array
    present_numbers = [False] * (n + 1)

    # Iterate through the input array and mark the corresponding indices in the boolean array as True
    for num in arr:
        present_numbers[num] = True

    # Find the first index in the boolean array that is False, which corresponds to the missing number
    for i in range(1, n + 1):
        if not present_numbers[i]:
            return i
        
       
 
# time complexity = O(n), and space complexity = O(1)
def find_missing_number_3(arr, n):
    total_sum = (n*(n+1)/2)
    arr_sum = 0
    
    for num in arr :
        arr_sum += num
    
    return int(total_sum - arr_sum)

# using xor method
def find_missing_num_4(arr, n):
    # XOR all the numbers in the range 0 to n
    xor = 0
    for i in range(n + 1):
        xor ^= i

    # XOR all the numbers in the array
    for num in arr:
        xor ^= num

    # The final result is the missing number
    return xor
    
print(find_missing_num_4(arr, N))
                

