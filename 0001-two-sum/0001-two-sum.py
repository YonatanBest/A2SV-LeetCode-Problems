class Solution:
    def twoSum(self, nums: List[int], target: int):
        find = defaultdict(int)
        for j in range(len(nums)):
            if target - nums[j] in find:
                return [find[target-nums[j]], j]
            find[nums[j]] = j
        return -1