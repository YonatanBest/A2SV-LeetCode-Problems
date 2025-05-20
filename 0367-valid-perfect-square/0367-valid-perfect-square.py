class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 0
        right = num//2 + 1
        mid = (left + right)//2

        def valid(mid):
            if mid * mid <= num:
                return True
            return False

        while left <= right:
            if valid(mid):
                left = mid + 1
                ans = mid
            else:
                right = mid - 1
            mid = (left + right)//2
        
        return ans*ans == num