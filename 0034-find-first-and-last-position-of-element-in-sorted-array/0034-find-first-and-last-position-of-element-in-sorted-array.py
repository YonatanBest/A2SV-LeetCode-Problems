class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums) - 1
        mid = (i + j)//2
        fpos = -1
        lpos = -1
        def first_pos(i, j, mid):
            nonlocal fpos
            if i > j:
                return
            if nums[mid] < target:
                i = mid + 1
            else:
                if nums[mid] == target:
                    fpos = mid
                j = mid - 1
            mid = (i + j)//2
            first_pos(i, j, mid)
            return
        def last_pos(i, j, mid):
            nonlocal lpos
            if i > j:
                return
            if nums[mid] > target:
                j = mid - 1
            else:
                if nums[mid] == target:
                    lpos = mid
                i = mid + 1
            mid = (i + j)//2
            last_pos(i, j, mid)
            return
        first_pos(i, j, mid)
        last_pos(i, j, mid)
        return [fpos, lpos]