class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        res = []
        for i in range(len(nums) - k + 1):
            arr = nums[i:k + i]
            print(arr)
            state = True
            for j in range(1, len(arr)):
                if arr[j] - arr[j - 1] != 1:
                    state = False
                    break
            if state:
                res.append(arr[len(arr) - 1])
            else:
                res.append(-1)
        return res