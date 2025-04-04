# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dic = defaultdict(int)
        for num in nums:
            if num in dic:
                total = sum(nums) - num
                lost = (len(nums)*(len(nums)+1))//2 - total
                return [num, lost]
            dic[num] += 1
        return []