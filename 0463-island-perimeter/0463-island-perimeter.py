class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        total_per = 0
        dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        
        def island(i, j, visited):
            nonlocal total_per

            if (i, j) in visited:
                return
            
            visited.add((i, j))

            for dl, dr in dir:
                if i + dl >= 0 and i + dl < len(grid) and j + dr >= 0 and j + dr < len(grid[0]):
                    if not grid[i + dl][j + dr]:
                        total_per += 1
                    else:
                        island(i + dl, j + dr, visited)
                else:
                    total_per += 1
            return



        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]:
                    island(i, j, set())
                    return total_per
        return 0
            