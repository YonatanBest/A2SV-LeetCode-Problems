class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        ans = [1,1]
        temp = 0
        while rowIndex != 1:
            ans.append(1)
            for i in range(1, len(ans) - 1):
                c = ans[i]
                if i != 1:
                    ans[i] = ans[i] + ans[i - 1] - temp
                else:
                    ans[i] = ans[i] + ans[i - 1]
                temp = ans[i] - c
            temp = 0
            rowIndex -= 1
        return ans


