class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        dir = [(-1,1), (1,-1)]
        arr = []
        row = 0
        col = 0
        di = 0
        print(len(mat))
        for i in range(len(mat)*len(mat[0])):
            arr.append(mat[row][col])
            if di == 0:
                if row - 1 < 0 or col + 1 >= len(mat[0]):
                    di = 1
                    if col + 1 >= len(mat[0]):
                        row += 1
                    else:
                        col += 1
                else:
                    row += dir[di][0]
                    col += dir[di][1]
            else:
                if col - 1 < 0 or row + 1 >= len(mat):
                    di = 0
                    if row + 1 >= len(mat):
                        col += 1
                    else:
                        row += 1
                else:
                    row += dir[di][0]
                    col += dir[di][1]
        return arr
