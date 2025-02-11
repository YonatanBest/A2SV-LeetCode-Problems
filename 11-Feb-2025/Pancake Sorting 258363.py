# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

import copy
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        new = copy.deepcopy(arr)
        ans = []
        length = len(arr)
        while length > 0:
            max_num = 0
            for i in range(length):
                if arr[max_num] < arr[i]:
                    max_num = i
            arr[0:max_num + 1] = reversed(arr[0:max_num + 1])
            ans.append(max_num + 1)
            arr[0:length] = reversed(arr[0:length])
            ans.append(length)
            length -= 1
        if new == arr:
            return []
        return ans
