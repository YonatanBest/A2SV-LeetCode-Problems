class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]
        suffix = [nums[-1]]
        for i in range(1, len(nums)):
            prefix.append(prefix[-1]*nums[i])
        for i in range(len(nums) - 2, -1, -1):
            suffix.append(suffix[-1]*nums[i])
        suffix.reverse()
        print(prefix)
        print(suffix)
        for i in range(len(nums)):
            if i - 1 >= 0 and i + 1 < len(nums):
                nums[i] = prefix[i - 1] * suffix[i + 1]
            elif i - 1 >= 0:
                nums[i] = prefix[i - 1]
            else:
                nums[i] = suffix[i + 1]
        return nums