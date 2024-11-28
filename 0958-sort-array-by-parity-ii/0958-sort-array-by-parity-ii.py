class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd = []
        even = []
        for i in nums:
            if i % 2:
                odd.append(i)
            else:
                even.append(i)
        print(even, odd)
        x = 0
        for j in range(0, len(nums), 2):
            nums[j] = even[x]
            x += 1
        x = 0
        for k in range(1, len(nums), 2):
            nums[k] = odd[x]
            x += 1
        return nums
