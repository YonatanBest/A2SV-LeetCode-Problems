# Problem: Max Consecutive Ones III - https://leetcode.com/problems/max-consecutive-ones-iii/

from collections import defaultdict
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        dic = defaultdict(int)
        chance = k
        i = 0
        j = 0
        max_len = 0

        while j < len(nums):      
            if nums[j] == 1:
                dic[1] += 1
            else:
                max_len = max(max_len, dic[1])
                if chance > 0:
                    dic[1] += 1
                    chance -= 1
                else:
                    while nums[i] != 0:
                        dic[1] -= 1
                        i += 1
                    dic[1] -= 1
                    i += 1
                    chance = 1
                    j -= 1
            j += 1
        max_len = max(max_len, dic[1])
        return max_len