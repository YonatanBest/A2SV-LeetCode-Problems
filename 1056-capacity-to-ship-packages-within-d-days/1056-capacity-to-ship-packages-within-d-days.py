class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def validate(mid):
            count = 1
            currmass = 0
            for weigh in weights:
                currmass += weigh
                if currmass > mid:
                    count += 1
                    currmass = weigh
                if count > days:
                    return False
            return True
        i = max(weights)
        j = sum(weights)
        mid = (i + j)//2
        ans = -1
        while i <= j:
            if validate(mid):
                ans = mid
                j = mid - 1
            else:
                i = mid + 1
            mid = (i + j)//2
        return ans
