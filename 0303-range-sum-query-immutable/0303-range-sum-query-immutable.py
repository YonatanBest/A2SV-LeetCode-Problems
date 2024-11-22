class NumArray:
    def __init__(self, nums: List[int]):
        self.total = [0]
        for i in nums:
            self.total.append(self.total[len(self.total) - 1] + i)

    def sumRange(self, left: int, right: int) -> int:
        self.res = 0
        self.res = self.total[right + 1] - self.total[left]
        return self.res


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)