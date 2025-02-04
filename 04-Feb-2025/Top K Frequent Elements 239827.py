# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        rep = Counter(nums)
        rep_desc = dict(sorted(rep.items(), key=lambda item: item[1], reverse=True))
        x = 0
        res = []
        for i in rep_desc:
            x += 1
            res.append(i)
            if x == k:
                break
        return res