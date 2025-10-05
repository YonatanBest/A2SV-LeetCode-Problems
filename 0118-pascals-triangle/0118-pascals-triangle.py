class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        if numRows == 1:
            return ans
        ans.append([1, 1])
        while len(ans) < numRows:
            temp = [1]
            for j in range(1, len(ans[-1])):
                temp.append(ans[-1][j] + ans[-1][j-1])
            temp.append(1)
            ans.append(temp.copy())
        return ans