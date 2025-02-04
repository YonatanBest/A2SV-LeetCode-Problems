from collections import Counter
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        rep = Counter(nums)
        res = []
        for i in rep:
            if rep[i] > 1:
                res.append(i)
        return res