# find the number in an array that appears ones

arr = [1,1,2,2,3,4,4,5,5]


def find_ones_1(arr):
    n = len(arr)
    maximum_num = arr[-1] # assume arr is sorted
    hashing = [0]*(maximum_num+1)

    for i in range(n):
        hashing[arr[i]]+= 1
        
    for i in range(1, n):
        if hashing[i] == 1:
            return i
    



def find_ones(arr):
    n = len(arr)
    mapping = {}
    
    for i in range(n):
        mapping[arr[i]] = mapping.get(arr[i], 0)+1
    
    for num, count in mapping.items():
        if count == 1:
            return num
    
   
   
   
# optimal solution    
def find_one_(arr):
    n = len(arr)
    xor = 0
    
    for i  in range(n):
        xor = xor ^ arr[i]
    
    return xor
    
print(find_one_(arr))