from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 2:
            return nums[0]
        majority = ceil(len(nums)/2)
        rep = Counter(nums)
        for i in rep:
            if rep[i] >= majority:
                return i