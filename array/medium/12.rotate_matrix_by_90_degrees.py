'''
Brute Force Approach

Algorithm / Intuition:
Approach: Take another dummy matrix of n*n, and then take the first row of the matrix and put it in the last column of
the dummy matrix, take the second row of the matrix, and put it in the second last column of the matrix and so.

Complexity Analysis
Time Complexity: O(N*N) to linearly iterate and put it into some other matrix.

Space Complexity: O(N*N) to copy it into some other matrix.

'''

from typing import List
def rotate(matrix: List[List[int]]) -> List[List[int]]:
    n = len(matrix)
    rotated = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated[j][n - i - 1] = matrix[i][j]
    return rotated




if __name__ == "__main__":
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotated = rotate(arr)
    print("Rotated Image")
    for i in range(len(rotated)):
        for j in range(len(rotated[0])):
            print(rotated[i][j], end=" ")
        print()
        
        
################################################



'''
Optimal Approach
Algorithm / Intuition
Intuition: By observation, we see that the first column of the original matrix is the reverse of the first row of the 
rotated matrix, so that’s why we transpose the matrix and then reverse each row, and since we are making changes in 
the matrix itself space complexity gets reduced to O(1).

Approach:

Step 1: Transpose the matrix. (transposing means changing columns to rows and rows to columns)

Step 2: Reverse each row of the matrix.
'''

from typing import List
def rotate(matrix: List[List[int]]) -> None:
    n = len(matrix)
    # transposing the matrix
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # reversing each row of the matrix
    for i in range(n):
        matrix[i].reverse()




if __name__ == "__main__":
    arr = [[1, 2, 3], 
           [4, 5, 6], 
           [7, 8, 9]]
    rotate(arr)
    print("Rotated Image")
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j], end=" ")
        print()
