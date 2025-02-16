# Problem: Tuple with Same Product - http://leetcode.com/problems/tuple-with-same-product

from collections import defaultdict
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        res = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] * nums[j] in dic:
                    res += dic[nums[i] * nums[j]]
                dic[nums[i] * nums[j]] += 1
        return res * 8