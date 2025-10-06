class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = defaultdict(int)

        for num in nums:
            majority[num] += 1
            if majority[num] > len(nums)/2:
                return num