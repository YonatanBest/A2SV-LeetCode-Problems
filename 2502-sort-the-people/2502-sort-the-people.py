class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dic = {}
        for times in range(len(heights)):
            min_curr = times
            i = times + 1
            while i < len(heights):
                if heights[i] > heights[min_curr]:
                    min_curr = i
                i += 1
            heights[times], heights[min_curr] = heights[min_curr], heights[times]
            names[times], names[min_curr] = names[min_curr], names[times]
        return names