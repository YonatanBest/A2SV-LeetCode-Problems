class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        max_area = 0
        curr_area = 0
        visited = set()

        def explore(i, j):
            nonlocal visited
            nonlocal curr_area

            if (i, j) in visited:
                return
            
            visited.add((i, j))
            curr_area += 1

            for dl, dr in dir:
                if i + dl >= 0 and i + dl < len(grid) and j + dr >= 0 and j + dr < len(grid[0]) and grid[i + dl][j + dr]:
                    explore(i + dl, j + dr)

            return

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and (i, j) not in visited:
                    curr_area = 0
                    explore(i, j)
                    max_area = max(max_area, curr_area)

        return max_area
        

