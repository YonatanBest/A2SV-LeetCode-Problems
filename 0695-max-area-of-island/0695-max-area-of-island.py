class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dir = [(-1,0),(1,0),(0,-1),(0,1)]
        max_area = 0
        visited = set()
        temp = 1
        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        def traverse(row, col):
            nonlocal max_area
            nonlocal visited
            nonlocal temp
            if (row, col) in visited:
                return
            visited.add((row, col))
            for i, j in dir:
                new_row, new_col = row + i, col + j
                if inbound(new_row, new_col):
                    if (new_row, new_col) in visited:
                        continue
                    if grid[new_row][new_col]:
                        temp += 1
                        traverse(new_row, new_col)
            max_area = max(temp, max_area)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    traverse(i, j)
                temp = 1
        return max_area


