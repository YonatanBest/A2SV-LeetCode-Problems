class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = defaultdict(int)
        for num in nums:
            majority[num] += 1

        ans = sorted(majority.items(), key= lambda x: x[1], reverse=True)
        return ans[0][0]