class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        key = {}
        dic = {}
        res = [0]*len(nums)
        for j in sorted(nums):
            if j in dic:
                dic[j] += 1
            else:
                dic[j] = 1
        for i in range(len(nums)):
            if nums[i] in key:
                key[nums[i]].append(i)
            else:
                key[nums[i]] = [i]
        curr = 0
        for k in dic:
            for i in range(dic[k]):
                res[key[k][i]] = curr
            curr += dic[k]
        return res