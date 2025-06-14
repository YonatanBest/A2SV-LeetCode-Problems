class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        if len(nums) == 1:
            return [str(nums[0])]
        nums.sort()
        ans = []
        temp = [] 
        for j in range(1, len(nums)):
            if nums[j] - nums[j - 1] == 1:
                temp.append(nums[j - 1])
                temp.append(nums[j])
                if j == len(nums) - 1:
                    ans.append(str(temp[0]) + "->" + str(temp[-1]))
            else:
                temp.append(nums[j - 1])
                if len(temp) > 1:
                    ans.append(str(temp[0]) + "->" + str(temp[-1]))
                else:
                    ans.append(str(temp[0]))
                temp = []
                if j == len(nums) - 1:
                    ans.append(str(nums[j]))
            
        return ans
