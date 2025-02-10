class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dic = {}
        for i in range(len(names)):
            dic[heights[i]] = names[i]
        for times in range(len(heights)):
            check = True
            for i in range(1, len(heights) - times):
                if heights[i - 1] < heights[i]:
                    heights[i - 1], heights[i] = heights[i], heights[i - 1]
                    check = False
            if check:
                break
        names = []
        for j in heights:
            names.append(dic[j])
        return names