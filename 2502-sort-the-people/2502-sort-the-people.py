class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        temp = len(heights) - 2
        while temp >= 0:
            times = temp
            i = times + 1
            while i < len(heights):
                if heights[times] < heights[i]:
                    heights[times], heights[i] = heights[i], heights[times]
                    names[times], names[i] = names[i], names[times]
                    times += 1
                i += 1
            temp -= 1
        return names