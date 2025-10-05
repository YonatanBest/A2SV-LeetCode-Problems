class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1]
        for j in range(rowIndex):
            temp = [1]
            for j in range(1, len(ans)):
                temp.append(ans[j] + ans[j - 1])
            temp.append(1)
            ans = temp.copy()
        return ans
        