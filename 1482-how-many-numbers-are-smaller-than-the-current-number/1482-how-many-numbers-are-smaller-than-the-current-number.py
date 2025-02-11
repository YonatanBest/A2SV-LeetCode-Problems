class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        new = sorted(nums)
        dic = {}
        for i in range(len(new)):
            if new[i] not in dic:
                dic[new[i]] = i
        for k in range(len(nums)):
            nums[k] = dic[nums[k]]
        return nums