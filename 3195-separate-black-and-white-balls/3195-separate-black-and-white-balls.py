class Solution:
    def minimumSteps(self, s: str) -> int:
        arr = list(s)
        count = 0
        ones = 0
        for i in s:
            if i == "1":
                ones += 1
            else:
                count += ones
        return count