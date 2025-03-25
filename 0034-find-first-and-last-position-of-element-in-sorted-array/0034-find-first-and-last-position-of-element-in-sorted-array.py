class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums) - 1
        mid = (i + j)//2
        fpos = -1
        lpos = -1
        def first_pos(i, j, mid):
            if i > j:
                return i
            if nums[mid] < target:
                i = mid + 1
            else:
                if nums[mid] == target:
                    fpos = mid
                j = mid - 1
            mid = (i + j)//2
            return first_pos(i, j, mid)
        def last_pos(i, j, mid):
            if i > j:
                return j
            if nums[mid] > target:
                j = mid - 1
            else:
                if nums[mid] == target:
                    lpos = mid
                i = mid + 1
            mid = (i + j)//2
            return last_pos(i, j, mid)
        fpos = first_pos(i, j, mid)
        lpos = last_pos(i, j, mid)
        if fpos < len(nums) and nums[fpos] == target:
            return [fpos, lpos]
        return [-1,-1]