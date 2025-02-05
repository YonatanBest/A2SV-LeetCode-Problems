from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        rep = Counter(nums)
        ans = []
        for i in rep:
            if rep[i] == 2:
                ans.append(i)
        return ans