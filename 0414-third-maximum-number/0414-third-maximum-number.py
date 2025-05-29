from collections import Counter
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        distinict = list(set(nums))
        distinict.sort(reverse=True)
        if len(distinict) < 3:
            return distinict[0]
        else:
            return distinict[2]
        