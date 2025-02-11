class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        ans = 0
        for i in grid:
            ans += max(i)
        count = 0
        for j in range(len(grid)):
            temp = []
            for k in range(len(grid[j])):
                temp.append(grid[k][j])
                if grid[k][j] > 0:
                    count += 1
            ans += max(temp)
        ans += count
        return ans