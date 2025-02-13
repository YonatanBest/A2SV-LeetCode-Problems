class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        k = len(nums) - 1
        closest_sum = sum(nums[:3])
        while k >= 2:
            i = 0
            j = k - 1
            while i < j:
                curr_sum = nums[i] + nums[j] + nums[k]
                if curr_sum == target:
                    return curr_sum
                elif curr_sum < target:
                    i += 1
                else:
                    j -= 1
                if abs(closest_sum - target) > abs(curr_sum - target):
                    closest_sum = curr_sum
            k -= 1

        return closest_sum