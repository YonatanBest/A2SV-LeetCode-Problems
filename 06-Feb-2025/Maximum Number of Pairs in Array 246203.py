# Problem: Maximum Number of Pairs in Array - https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

from collections import Counter
class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        rep = Counter(nums)
        pair = 0
        left = 0
        for i in rep:
            left += rep[i] % 2
            pair += rep[i] // 2
        return [pair, left]
