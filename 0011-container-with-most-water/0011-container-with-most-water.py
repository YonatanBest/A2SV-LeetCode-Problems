class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        max_area = 0
        while i < j:

            max_area = max((j - i) * min(height[j] , height[i]), max_area)

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        
        return max_area