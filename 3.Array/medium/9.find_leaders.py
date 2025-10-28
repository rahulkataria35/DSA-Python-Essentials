'''
Coding Ninja >> https://www.codingninjas.com/studio/problems/superior-elements_6783446?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf

Problem Statement: Given an array, print all the elements which are leaders. 
A Leader is an element that is greater than all of the elements on its right side in the array. [element, >>>]
Example:
Input:
arr = [10, 22, 12, 3, 0, 6]
Output:
22 12 6
Explanation:
6 is a leader. In addition to that, 12 is greater than all the elements in its right side (3, 0, 6), also 22 is greater than 12, 3, 0, 6.
'''

# find leaders in an array: everything on the right should be smaller

def leader(arr):
    n = len(arr)
    leaders = []
    for i in range(n):
        flag = True
        for j in range(i, n):
            if arr[j] > arr[i]:
                flag = False
                break
        if flag :
            leaders.append(arr[i])
    return leaders


def reverse(arr):
    s = 0 
    end = len(arr) -1
    while s<end:
        arr[s], arr[end] = arr[end], arr[s]
        s += 1
        end -= 1
    return arr
    
def find_leader(arr):
    n = len(arr)
    ans = []
    maximum = float('-inf')
    # Last element of an array is always a leader,

    for i in range(n-1, 0, -1):
        if arr[i] > maximum:
            ans.append(arr[i])
            maximum = arr[i]
            
    # if the user want the result in an order
    return reverse(ans)
    
arr = [10,22,12,3,0,6]

print(find_leader(arr))