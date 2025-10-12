
# Time complexity: O(n)
# - The loop runs n times, where n is the length of the array.
# - Adding an element to a set has an average time complexity of O(1).
# - Converting the set to a list takes O(n) time.

# Space complexity: O(n)
# - The set `s` can contain at most n elements in the worst case.
# - The list conversion also takes O(n) space.

def remove_duplicate_1(arr):
    n = len(arr)
    s = set()
    for i in range(n):
        s.add(arr[i])
    return list(s)



# Time complexity: O(n log n)
# - Sorting the array takes O(n log n) time.
# - The loop runs n times, where n is the length of the array, which takes O(n) time.
# - Overall, the time complexity is dominated by the sorting step, so it is O(n log n).

# Space complexity: O(1)
# - The algorithm modifies the array in place and uses only a constant amount of extra space.
# if arr comes in sorted way
def remove_duplicate_2(arr):
    arr.sort()
    i = 0
    for j in range(1, len(arr)):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]
            
    # lenth of the unique element is (i+1)
    i = i + 1
    return arr[:i]

# Time complexity: O(n)
# - Creating a set from the list takes O(n) time, where n is the length of the array.
# - Converting the set back to a list also takes O(n) time.
# - Overall, the time complexity is O(n).

# Space complexity: O(n)
# - The set can contain at most n elements in the worst case.
# - The list conversion also takes O(n) space.
def remove_duplicate_3(arr):
    return list(set(arr))

arr = [1,2,3,2,1,3]

print(remove_duplicate_2(arr))