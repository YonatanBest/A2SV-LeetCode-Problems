class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        temp = Counter(nums)
        ans = []
        for j in temp:
            if temp[j] > len(nums)//3:
                ans.append(j)

        return ans