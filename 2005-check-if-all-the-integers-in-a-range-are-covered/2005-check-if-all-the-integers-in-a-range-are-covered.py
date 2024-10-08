class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        state = False
        for i in range(left, right + 1):
            for j in range(len(ranges)):
                if ranges[j][0] <= i and ranges[j][1] >= i:
                    state = True
                    break
                else:
                    state = False
            if state == False:
                return state
        return state