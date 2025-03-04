class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = []
        self.ans = []
        for i in nums:
            if not self.prefix_sum:
                self.prefix_sum.append(i)
            else:
                self.prefix_sum.append(self.prefix_sum[-1] + i)

    def sumRange(self, left: int, right: int) -> int:
        if left != 0:
            return self.prefix_sum[right] - self.prefix_sum[left - 1]
        
        return self.prefix_sum[right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)