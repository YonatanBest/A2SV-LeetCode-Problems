class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        left = 0
        right = 1290
        mid = (left + right) // 2
        def valid(mid):
            return 3**mid <= n
        ans = None
        while left <= right:
            if valid(mid):
                left = mid + 1
                ans = mid
            else:
                right = mid - 1
            mid = (left + right) // 2
        return 3**mid == n