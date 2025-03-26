class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        i = 1
        j = max(piles)
        mid = (i + j)//2
        ans = -1
        def validate(mid):
            hours = 0
            for bananas in piles:
                if hours > h:
                    return False
                hours += ceil(bananas/mid)
            return hours <= h
        while i <= j:
            if validate(mid):
                ans = mid
                j = mid - 1
            else:
                i = mid + 1
            mid = (i + j)//2
        return ans
