# Problem: Determine Whether Matrix Can Be Obtained By Rotation - https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        res = [[0 for col in range(len(mat))] for row in range(len(mat))]
        x = 0
        while x < 4:
            check = True
            for row in range(len(mat)):
                for col in range(len(mat)):
                    if mat[row][col] != target[row][col]:
                        check = False
                        break
                if not check:
                    break
            for i in range(len(mat)):
                for j in range(len(mat)):
                    res[j][len(mat) - i - 1] = mat[i][j]
            for i in range(len(mat)):
                for j in range(len(mat)):
                    mat[i][j] = res[i][j]
            x += 1
            if check:
                return True
        return False