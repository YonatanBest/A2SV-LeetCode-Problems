class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        total = 0
        dic = defaultdict(int)
        dic[0] += 1
        ans = 0
        for i in range(len(nums)):
            total += nums[i]
            ans += dic[total - goal]
            dic[total] += 1
        return ans