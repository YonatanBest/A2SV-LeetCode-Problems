# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res = 0
        ans = []
        for j in nums:
            if j % 2 == 0:
                res += j
        for i in queries:
            if nums[i[1]] % 2 == 0:
                res -= nums[i[1]]
            nums[i[1]] += i[0]
            if nums[i[1]] % 2 == 0:
                res += nums[i[1]]
            ans.append(res)

        return ans