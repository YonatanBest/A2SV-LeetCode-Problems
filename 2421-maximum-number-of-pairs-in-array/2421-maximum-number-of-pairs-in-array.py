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
