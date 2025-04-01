class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left, right):
            arr = []
            l = 0
            r = 0
            while l < len(left) and r < len(right):
                if left[l] <= right[r]:
                    arr.append(left[l])
                    l += 1
                else:
                    arr.append(right[r])
                    r += 1
            while l < len(left):
                arr.append(left[l])
                l += 1
             
            while r < len(right):
                arr.append(right[r])
                r += 1
            return arr

        def merge_sort(arr):
            if len(arr) == 1:
                return arr
            left = merge_sort(arr[:len(arr)//2])
            right =  merge_sort(arr[len(arr)//2:])
            return merge(left, right)
        return merge_sort(nums)
