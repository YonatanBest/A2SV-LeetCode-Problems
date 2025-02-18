class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        new = [0]*len(nums)
        dic = defaultdict(int)

        for i, j in requests:
            new[i] += 1
            if j + 1 < len(nums):
                new[j + 1] -= 1
        
        for k in range(1, len(new)):
            new[k] += new[k - 1]

        new.sort(reverse=True)
        nums.sort(reverse=True)
        max_sum = 0

        for i in range(len(new)):
            max_sum += new[i]*nums[i]

        return max_sum % (10**9 + 7)