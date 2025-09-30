class Solution:
    def twoSum(self, nums: List[int], target: int):
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic:
                dic[nums[i]].append(i)
            else:
                dic[nums[i]] = [i]
        nums.sort()
        i = 0
        j = len(nums) - 1
        while i < j:
            if nums[i] + nums[j] == target:
                if nums[i] == nums[j]:
                    return [dic[nums[i]][0], dic[nums[i]][1]]
                else:
                    return [dic[nums[i]][0], dic[nums[j]][0]]
            elif nums[i] + nums[j] > target:
                j -= 1
            else:
                i += 1
        return -1
            