class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0]*len(temperatures)

        for j in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[j]:
                ans[stack.pop()] = j - stack[-1]
            stack.append(j)
        return ans