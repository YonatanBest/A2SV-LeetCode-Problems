class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic:
                dic[nums[i]].append(i)
            else:
                dic[nums[i]] = [i]
        nums.sort()
        if nums[-2] != 0 and nums[-1]/nums[-2] >= 2:
            return dic[nums[-1]][0]
        elif nums[-2] == 0 and nums[-1] != 0:
            return dic[nums[-1]][0]
        else:
            return -1