'''
Coding Ninja :>  https://www.codingninjas.com/studio/problems/4sum_5713771?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
LeetCode : > https://leetcode.com/problems/4sum/
Problem Statement: Given an array of N integers, your task is to find unique quads that add up to give a target value.
In short, you need to return an array of all the unique quadruplets [arr[a], arr[b], arr[c], arr[d]] such that their sum is equal to a given target.

Note:
0 <= a, b, c, d < n
a, b, c, and d are distinct.
arr[a] + arr[b] + arr[c] + arr[d] == target

Example :
Input Format: arr[] = [1,0,-1,0,-2,2], target = 0
Result: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Explanation: We have to find unique quadruplets from the array such that the sum of those elements is equal to the target sum given that is 0. 
The result obtained is such that the sum of the quadruplets yields 0.
'''

# Brute Force 
def sumBF(arr,target):
    # Here I was not getting the ans because the of k { compiler was taking the for loop k, because I had same name for 2 variable}
    n = len(arr)
    aSet = set() 
    for i in range (n):
        for j in range (i+1, n):
            for k in range (j+1, n):
                for l in range (k+1, n):
                    sum = arr[i] + arr[j] 
                    sum += arr[k] 
                    sum += arr[l]
                    
                    if sum == target  :
                    # if arr[i] +arr[j] +arr[k] +arr[l] == k +1:
                        temp = [arr[i], arr[j], arr[k], arr[l]] 
                        temp.sort() 
                        aSet.add(tuple(temp))
                        
    ans = [list(e) for e in aSet]
    return ans
  

# Test Run 
# print (sumBF([4,3,3,4,4,2,1,2,1,1],9))

# Better Approach >> Using 3 For loop and a dictionary 
def sumBA (arr,target):
    n = len(arr)
   
    aSet = set()
    for i in range (n): 
        for j in range (i+1, n):
            # For 3 sum it will be inside first for loop 
            store = set()
            for k in range (j+1,n) :
                sum = arr[i] + arr[j] +arr[k]
                fourth = target - sum  
                
                if fourth in store :
                    temp = [arr[i], arr[j], arr[k], fourth]
                    temp.sort() 
                    aSet.add(tuple(temp))
                store.add(arr[k])
                    
    ans = [list(e) for e in aSet]
    return ans           


# Test Run 
# print (sumBA([4,3,3,4,4,2,1,2,1,1],9))         

# Optimal Approach  > using pointers 

def sumOA (nums, target):
    nums.sort()
    n = len(nums)
    ans = []
    
    for i in range (n):
        if i >0 and nums[i] == nums[i-1]:
            continue 
        for j in range (i+1, n):
            if j > i+1  and nums[j] == nums[j - 1]:
                continue 
             
            k = j+1 
            l = n-1 
            
            while (k < l):
                
                tempSum = nums[i] +nums[j] +nums[k] + nums[l]
                
                if tempSum == target :
                    tempArr = [nums[i],nums[j], nums[k], nums[l]]
                    ans.append(tempArr)
                    k += 1 
                    l -= 1
                
                    # Skiping the duplicate values 
                    while (k <l ) and nums[k] == nums[k-1]:
                        k += 1
                    while (k < l) and nums[l] == nums[l+1]:
                        l -= 1
                elif tempSum < target :
                    k += 1
                else :
                    l -= 1
    return ans  
# Test Run 
print (sumOA([4,3,3,4,4,2,1,2,1,1],9))    