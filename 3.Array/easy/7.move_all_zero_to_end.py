'''
Problem :  You are given an array of integers, your task is to move all the zeros in the array to the end of the array and
move non-negative integers to the front by maintaining their order.

Example :
Input: 1 ,0 ,2 ,3 ,0 ,4 ,0 ,1
Output: 1 ,2 ,3 ,4 ,1 ,0 ,0 ,0
Explanation: All the zeros are moved to the end and non-negative integers are moved to front by maintaining order


'''

arr = [1,3,0,2,0,4,5,8,0,1,3,0,3]

def move_all_zero_to_the_end_1(arr):
    zeros = []
    non_zeros = []
    for i in range(len(arr)):
        if arr[i] > 0:
            non_zeros.append(arr[i])
        else:
            zeros.append(arr[i])

    return non_zeros + zeros

def move_all_zero_to_the_end_2(arr):
    temp = []
    for i in range(len(arr)):
        if arr[i] > 0:
            temp.append(arr[i])
    zeros = len(arr)-len(temp)
    for i in range(zeros):
        temp.append(0)
    return temp
    
    
###########################################################

# optimal approach
# arr = [1,3,0,2,0,4,5,8,0,1,3,0,3]

def move_all_zero_to_the_end_3(arr):
    n = len(arr)
    j = -1
    
    for i in range(n):
        if arr[i] == 0:
            j = i
            break
    
    if j == -1: # means no zero in the array
        return arr

    for i in range(j+1,n):
        if arr[i] != 0:
            arr[j] = arr[i]
            arr[i] = 0
            j += 1
    return arr


print(move_all_zero_to_the_end_3(arr))


# move all zeros to the end best solution
def move_zeros(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        if arr[i] != 0:
            arr[count], arr[i] = arr[i], arr[count]
            count += 1
    return arr
