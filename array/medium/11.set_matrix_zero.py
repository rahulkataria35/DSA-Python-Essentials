

# bruteforce approach
# Time Complexity: O((N*M)*(N + M)) + O(N*M),
# space complexity = O(1)
def markRow(matrix, n, m, i):
    # set all non-zero elements as -1 in the row i:
    for j in range(m):
        if matrix[i][j] != 0:
            matrix[i][j] = -1

def markCol(matrix, n, m, j):
    # set all non-zero elements as -1 in the col j:
    for i in range(n):
        if matrix[i][j] != 0:
            matrix[i][j] = -1


def set_zero(matrix, rows, cols):
    # set -1 for rows and cols that contain 0, and don't mark any zero as -1
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                # mark the rows and cols containing 0
                markRow(matrix, rows, cols, i)
                markCol(matrix, rows, cols, j)
    
    # finally, mark all -1 as 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == -1:
                matrix[i][j] = 0
    return matrix

matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
n = len(matrix)
m = len(matrix[0])
ans = set_zero(matrix, n, m)
for row in ans:
    for ele in row:
        print(ele, end=" ")
    print()
    
######################################################################
# better approach
# Time Complexity: O(2*(N*M)), 
# Space Complexity: O(N) + O(M), 
def zeroMatrix(matrix, n, m):
    row = [0] * n  # row array
    col = [0] * m  # col array

    # Traverse the matrix:
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                # mark ith index of row wih 1:
                row[i] = 1

                # mark jth index of col wih 1:
                col[j] = 1

    # Finally, mark all (i, j) as 0
    # if row[i] or col[j] is marked with 1.
    for i in range(n):
        for j in range(m):
                if row[i] or col[j]:
                    matrix[i][j] = 0

    return matrix

matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
n = len(matrix)
m = len(matrix[0])
ans = zeroMatrix(matrix, n, m)

print("The Final matrix is:")
for row in ans:
    for ele in row:
        print(ele, end=" ")
    print()
    
    
    
############################################

# optimise approach
# Time Complexity: O(2*(N*M)), 
# space complexity = O(1)
def zeroMatrix(matrix, n, m):
    # int row[n] = {0}; --> matrix[..][0]
    # int col[m] = {0}; --> matrix[0][..]

    col0 = 1
    # step 1: Traverse the matrix and
    # mark 1st row & col accordingly:
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                # mark i-th row:
                matrix[i][0] = 0

                # mark j-th column:
                if j != 0:
                    matrix[0][j] = 0
                else:
                    col0 = 0

    # Step 2: Mark with 0 from (1,1) to (n-1, m-1):
    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][j] != 0:
                # check for col & row:
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

    #step 3: Finally mark the 1st col & then 1st row:
    if matrix[0][0] == 0:
        for j in range(m):
            matrix[0][j] = 0
    if col0 == 0:
        for i in range(n):
            matrix[i][0] = 0

    return matrix


matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
n = len(matrix)
m = len(matrix[0])
ans = zeroMatrix(matrix, n, m)

print("The Final matrix is:")
for row in ans:
    for ele in row:
        print(ele, end=" ")
    print()


