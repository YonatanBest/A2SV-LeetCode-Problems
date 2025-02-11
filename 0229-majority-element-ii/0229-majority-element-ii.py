from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dic = Counter(nums)
        ans = []
        for i in dic:
            if dic[i] > len(nums)//3:
                ans.append(i)
        return ans