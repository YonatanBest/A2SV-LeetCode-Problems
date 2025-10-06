class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        temp = [nums[0], 1]
        majority = defaultdict(int)
        
        for num in nums:
            majority[num] += 1
            if temp[1] < majority[num]:
                temp = [num, majority[num]]

        return temp[0]