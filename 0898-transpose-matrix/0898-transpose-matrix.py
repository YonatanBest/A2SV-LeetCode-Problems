class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        arr = [[0 for i in range(len(matrix))] for i in range(len(matrix[-1]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                arr[j][i] = matrix[i][j]
        return arr