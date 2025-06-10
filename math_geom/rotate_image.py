# https://leetcode.com/problems/rotate-image/

# TC - O(M * N), SC - O(M * N)
def rotate(matrix):
    N = len(matrix)

    # Step 1: Transpose the matrix (swap elements across the main diagonal)
    for i in range(N):
        for j in range(i, N):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for i in range(N):
        matrix[i].reverse()

matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
rotate(matrix1)
print(matrix1)  # Expected: [[7,4,1],[8,5,2],[9,6,3]]

matrix2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
rotate(matrix2)
print(matrix2)  # Expected: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]