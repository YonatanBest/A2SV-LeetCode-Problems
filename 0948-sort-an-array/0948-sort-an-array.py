class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        bucket = [[], [], [], [], [], [], [], [], [], [], []]
        for i in nums:
            idx = i//10_000 + 5
            bucket[idx].append(i)
            # right = len(bucket[idx]) - 2
            # while right >= 0:
            #     if bucket[idx][right] > bucket[idx][right + 1]:
            #         bucket[idx][right], bucket[idx][right + 1] = bucket[idx][right + 1], bucket[idx][right]
            #         right -= 1
            #     else:
            #         break
        print(bucket)
        nums = []
        for arr in bucket:
            nums += sorted(arr)
        return nums