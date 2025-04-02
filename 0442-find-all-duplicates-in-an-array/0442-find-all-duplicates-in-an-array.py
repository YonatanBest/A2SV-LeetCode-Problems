class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        dic = {}
        for ele in nums:
            if ele not in dic:
                dic[ele] = 1
            else:
                ans.append(ele)
                del dic[ele]
        return ans