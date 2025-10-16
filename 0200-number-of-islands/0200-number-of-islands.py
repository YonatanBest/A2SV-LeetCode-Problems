class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()
        island_num = 0

        def explore(i, j):
            nonlocal visited

            if (i, j) in visited:
                return
            
            visited.add((i, j))

            for dl, dr in dir:
                if i + dl >= 0 and i + dl < len(grid) and j + dr >= 0 and j + dr < len(grid[0]):
                    if grid[i + dl][j + dr] == "1":
                        explore(i + dl, j + dr)
            
            return

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1" and (i, j) not in visited:
                    island_num += 1
                    explore(i, j)
        return island_num