class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        bucket = [[] for i in range(1_000)]
        for i in nums:
            idx = i//1_000 + 50
            bucket[idx].append(i)
            right = len(bucket[idx]) - 2
            while right >= 0:
                if bucket[idx][right] > bucket[idx][right + 1]:
                    bucket[idx][right], bucket[idx][right + 1] = bucket[idx][right + 1], bucket[idx][right]
                    right -= 1
                else:
                    break
        nums = []
        for arr in bucket:
            nums += arr
        return nums