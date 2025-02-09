class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dir = 0
        pos = [(0,1), (1,0), (0, -1), (-1, 0)]
        matrix_arr = []
        row = 0
        col = 0
        for i in range(len(matrix) * len(matrix[0])):
            matrix_arr.append(matrix[row][col])
            temp = [row, col]
            if dir == 0:
                if col + 1 >= len(matrix[0]) or matrix[row][col + 1] == None:
                    dir += 1
                    row += 1
                else:
                    col += 1
            elif dir == 1:
                if row + 1 >= len(matrix) or matrix[row + 1][col] == None:
                    dir += 1
                    col -= 1
                else:
                    row += 1
            elif dir == 2:
                if col - 1 < 0 or matrix[row][col - 1] == None:
                    dir += 1
                    row -= 1
                else:
                    col -= 1
            else:
                if row - 1 < 0 or matrix[row - 1][col] == None:
                    dir = 0
                    col += 1 
                else:
                    row -= 1
            matrix[temp[0]][temp[1]] = None
        return matrix_arr