class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        vote = [nums[0], 1]
        for j in range(1, len(nums)):
            
            if vote[0] == nums[j]:
                vote[1] += 1
            else:
                vote[1] -= 1
                if vote[1] == 0:
                    vote = [nums[j], 1]

        return vote[0]