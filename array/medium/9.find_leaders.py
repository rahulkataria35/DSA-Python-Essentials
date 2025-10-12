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