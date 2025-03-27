# Problem: Zero Array Transformation II - https://leetcode.com/problems/zero-array-transformation-ii/

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        if sum(nums) == 0:
            return 0

        def validate(mid):
            check = [0] * (len(nums))
            for que in range(mid):
                l, r, v = queries[que]
                check[l] -= v
                if r + 1 < len(nums):
                    check[r + 1] += v

            for k in range(1, len(nums)):
                check[k] += check[k - 1]
            
            for k in range(len(nums)):
                if check[k] + nums[k] > 0:
                    return False
            return True

        i = 1
        j = len(queries)
        mid = (i + j)//2
        temp = -1
        while i <= j:
            if validate(mid):
                temp = mid
                j = mid - 1
            else:
                i = mid + 1
            mid = (i + j) // 2
        return temp