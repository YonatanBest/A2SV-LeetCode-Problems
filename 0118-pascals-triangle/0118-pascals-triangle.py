class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        ans = [[1], [1, 1]]
        start = [1, 1]
        def pascal(test):
            new = [1,1]
            x = 0
            for i in range(1, len(test)):
                new.insert(1 + x, test[i - 1] + test[i])
                x += 1
            ans.append(new)
        for i in range(numRows - 2):
            test = ans[-1][:]
            pascal(test)
        return ans