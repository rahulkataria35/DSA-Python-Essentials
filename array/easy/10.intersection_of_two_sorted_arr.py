# intersection - present in both array

arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr2 = [2, 3, 4, 4, 5, 11, 12]

def intersection(arr1, arr2):
    return list(set(arr1) & set(arr2))


def intersection(arr1,arr2):
    return [value for value in arr1 if value in arr2]

# intersection - present in both arrays

def find_intersection(array1, array2):
    """
    This function finds the intersection of two input arrays, which are assumed to be lists of integers.
    The function first converts the second array to a set for faster lookup, and then iterates over
    the first array, checking if each element is in the set of the second array. If it is, the element
    is added to the result set. Finally, the result set is converted back to a list and returned.
    """
    set2 = set(array2)
    result = set()
    for num in array1:
        if num in set2:
            result.add(num)
    return list(result)




def intersection_1(arr1, arr2):
    i = 0
    j = 0
    result = []
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            # Move pointer of the smaller array
            i += 1
        elif arr1[i] > arr2[j]:
            # Move pointer of the larger array
            j += 1
        else:
            #If elements are equal, append it only if not a duplicate
            if not result or result[-1] != arr1[i]:
                result.append(arr1[i])
                # Move both pointers since duplicates are allowed
            i += 1
            j += 1
    return result



print(intersection_1(arr1, arr2))