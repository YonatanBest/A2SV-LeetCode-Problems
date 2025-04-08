class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        dir = [(-1,0), (0, -1), (1, 0), (0, 1)]
        perimeter = 0
        def inbound(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])
        def dfs(row, col, visited):
            nonlocal perimeter
            visited.add((row, col))
            for row_cha, col_cha in dir:
                new_row, new_col = row + row_cha, col + col_cha
                if inbound(new_row, new_col) and grid[new_row][new_col]:
                    if (new_row, new_col) not in visited:
                        dfs(new_row, new_col, visited)
                else:
                    perimeter += 1
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]:
                    dfs(r, c, set())  
                    return perimeter
        return perimeter