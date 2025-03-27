class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        temp = None
        i = 1
        j = max(ranks)*(cars**2)
        mid = (i + j)//2

        def validate(mid):
            carable = 0
            for rank in ranks:
                carable += int(sqrt(mid/rank))
            if carable < cars:
                return False
            return True

        while i <= j:
            if validate(mid):
                temp = mid
                j = mid - 1
            else:
                i = mid + 1
            mid = (i + j)//2
        return temp
        