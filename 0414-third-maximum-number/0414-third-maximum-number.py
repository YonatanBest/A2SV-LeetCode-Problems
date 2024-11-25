class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        if len(dic) >= 3:
           return sorted(dic)[len(dic) - 3]
        else:
            return sorted(dic)[len(dic) - 1]
        