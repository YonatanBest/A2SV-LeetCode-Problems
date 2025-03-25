class Solution:
    def mySqrt(self, x: int) -> int:
        i = 0
        j = x//2 + 1
        mid = (i + j)//2
        while i <= j:
            if mid*mid <= x and (mid+1)*(mid+1) > x:
                return mid
            elif mid*mid < x:
                i = mid + 1
            else:
                j = mid - 1
            mid = (i + j)//2
        return -1