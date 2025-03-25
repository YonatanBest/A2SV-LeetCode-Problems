# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        i = 1
        j = n
        mid = (i + j)//2
        while i <= j:
            if isBadVersion(mid):
                j = mid - 1
            else:
                i = mid + 1
            mid = (i + j)//2
        return i