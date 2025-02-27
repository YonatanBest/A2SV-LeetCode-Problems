# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 0
        j = int(sqrt(c))
        while i <= j:
            if i*i + j*j > c:
                j -= 1
            elif i*i + j*j < c:
                i -= 1
            else:
                return True
        return False