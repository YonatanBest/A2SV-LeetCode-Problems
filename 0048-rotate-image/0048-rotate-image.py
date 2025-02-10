class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        

        row  = len(matrix)
        col = len(matrix[0])




        # for c in range(col-1, -1, -1):
        #     for r in range(row):
        #         print(matrix[c][r], end=" ")


        res = [[0 for _ in range(col)] for _ in range(row)]
        

        new_col =col -1
        new_row = 0
        for r in range(row):
            for c in range(col):
                cur = matrix[r][c]
                res[new_row][new_col] = cur
                new_row+=1
            new_row = 0
            new_col-=1
        """
        

        0, 1-- > 1, 2

        i, j -- > j, n-i-1 -->  n-i-1, 
        j, n-i-1 --> n-i-1, n-j-1
        0, 0----> 0, 0-1
                  0, 3



        2, 3 --> 3, 1
        


        0, 1 ---> 1, 0 -->
        i, j--> n-j, 


        """
        for i in range(row):
            for j in range(col):
                matrix[i][j] = res[i][j]