# Problem: Two Sum - https://leetcode.com/problems/two-sum/description

from collections import Counter
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i in range(len(nums)):
            if nums[i] in nums_dict:
                nums_dict[nums[i]].append(i)
            else:
                nums_dict[nums[i]] = [i]
        nums.sort()
        i = 0
        j = len(nums) - 1
        while i < j:
            if nums[i] + nums[j] > target:
                j -= 1
            elif nums[i] + nums[j] < target:
                i += 1
            else:
                if nums[i] == nums[j]:
                    return [nums_dict[nums[i]][0], nums_dict[nums[i]][1]]
                else:
                    return [nums_dict[nums[i]][0], nums_dict[nums[j]][0]]
        return -1