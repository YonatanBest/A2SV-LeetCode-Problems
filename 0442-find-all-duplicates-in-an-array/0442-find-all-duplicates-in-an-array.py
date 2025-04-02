class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dic = Counter(nums)
        ans = []
        for i in dic:
            if dic[i] == 2:
                ans.append(i)
        return ans