class Solution:
    def search(self, nums: List[int], target: int) -> int:
        self.ans = -1
        i = 0
        j = len(nums) - 1
        mid = (i + j)//2
        def binarysearch(i, j, mid):
            if i > j:
                return -1
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                j = mid - 1
            else:
                i = mid + 1
            mid = (i + j)//2
            return binarysearch(i, j, mid)
        self.ans = binarysearch(i, j, mid)
        return self.ans
