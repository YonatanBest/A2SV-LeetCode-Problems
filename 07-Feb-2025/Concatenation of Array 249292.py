# Problem: Concatenation of Array - https://leetcode.com/problems/concatenation-of-array/description/

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(2):
            for j in nums:
                res.append(j)
        return res