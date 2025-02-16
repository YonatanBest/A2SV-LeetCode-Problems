# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(arr):
            if len(arr) > 1:
                left_arr = arr[:len(arr)//2]
                right_arr = arr[len(arr)//2:]
                
                merge_sort(left_arr)
                merge_sort(right_arr)

                left = 0
                right = 0
                new_index = 0

                while left < len(left_arr) and right < len(right_arr):
                    if left_arr[left] > right_arr[right]:
                        arr[new_index] = right_arr[right]
                        right += 1
                    else:
                        arr[new_index] = left_arr[left]
                        left += 1
                    new_index += 1
                while left < len(left_arr):
                    arr[new_index] = left_arr[left]
                    left += 1
                    new_index += 1
                while right < len(right_arr):
                    arr[new_index] = right_arr[right]
                    right += 1
                    new_index += 1

        merge_sort(nums)     
        return nums