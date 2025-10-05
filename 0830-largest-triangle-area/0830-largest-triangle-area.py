class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        
        max_area = 0
        def area(path):
            a = math.sqrt((path[0][0] - path[1][0])**2 + abs(path[0][1] - path[1][1])**2)
            b = math.sqrt((path[0][0] - path[2][0])**2 + abs(path[0][1] - path[2][1])**2)
            c = math.sqrt((path[2][0] - path[1][0])**2 + abs(path[2][1] - path[1][1])**2)
            s = (a+b+c)/2
            if s*(s-a)*(s-b)*(s-c) < 0:
                return 0
            area = math.sqrt(s*(s-a)*(s-b)*(s-c))
            return area
        def find(path, j):
            nonlocal max_area
            if len(path) == 3:
                max_area = max(max_area, area(path))
                return
            
            for i in range(j, len(points)):
                path.append(points[i])
                find(path, i + 1)
                path.pop()
            return
        find([], 0)
        return max_area