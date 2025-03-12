class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        self.new = [1]
        def pascal(ans, x):
            print(ans, x)
            if x == 0:
                return ans
            if x == 1:
                print("ans")
                self.new = ans
                return ans
            temp = 0
            ans.append(1)
            for i in range(1, len(ans) - 1):
                c = ans[i]
                if i != 1:
                    ans[i] = ans[i] + ans[i - 1] - temp
                else:
                    ans[i] = ans[i] + ans[i - 1]
                temp = ans[i] - c
            temp = 0
            pascal(ans, x - 1)
        pascal([1,1], rowIndex)
        return self.new


