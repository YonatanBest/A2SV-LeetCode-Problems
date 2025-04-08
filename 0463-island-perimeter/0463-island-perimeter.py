class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        dir = [(-1,0), (0, -1), (1, 0), (0, 1)]
        total_row = len(grid)
        total_col = len(grid[0])
        perimeter = 0
        for i in range(total_row):
            for j in range(total_col):
                if grid[i][j]:
                    for x, y in dir:
                        if 0 <= i + x < total_row and 0 <= j + y < total_col:
                            if not grid[i + x][j + y]:
                                perimeter += 1
                        else:
                            perimeter += 1
                    print(perimeter, i, j)
        return perimeter

            