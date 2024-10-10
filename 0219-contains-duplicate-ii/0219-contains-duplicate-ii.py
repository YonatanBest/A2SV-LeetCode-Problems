class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ans = {}
        for i in range(len(nums)):
            if nums[i] in ans:
                ans[nums[i]].append(i)
            else:
                 ans[nums[i]] = [i]
        print(ans)
        for i in ans:
            test = float("inf")
            for j in range(1, len(ans[i])):
                test = min(test, abs(ans[i][j - 1] - ans[i][j]))
            if test <= k:
                return True
        return False