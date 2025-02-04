# Problem: Plus One - https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = "".join(list(map(str, digits)))
        num = int(num) + 1
        digits = []
        for i in str(num):
            digits.append(int(i))
        return digits