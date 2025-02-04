from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = ceil(len(nums)/2)
        rep = Counter(nums)
        for i in rep:
            if rep[i] >= majority:
                return i