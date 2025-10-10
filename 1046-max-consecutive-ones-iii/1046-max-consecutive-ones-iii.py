class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_ones = 0
        count = defaultdict(int)
        i = 0
        j = 0

        while j < len(nums):
            if nums[j]:
                count[1] += 1
            else:
                while not k and i <= j:
                    if not nums[i]:
                        k += 1
                    count[nums[i]] -= 1
                    i += 1

                if k:
                    k -= 1
                    count[0] += 1
                else:
                    count = defaultdict(int)

            max_ones = max(max_ones, count[0] + count[1])
            j += 1

        return max_ones