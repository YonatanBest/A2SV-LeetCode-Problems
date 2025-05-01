class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        graph = [[] for j in range(n)]
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    graph[i].append(j)
                    graph[j].append(i)
        ans = 0
        visited = set()
        master = set()
        def traverse(node, visited):
            nonlocal master
            nonlocal ans
            if not graph:
                return True
            if node in master:
                return False
            if node in visited:
                return True
            visited.add(node)
            for j in graph[node]:
                if not traverse(j, visited):
                    return False
            return visited
        for j in range(n):
            temp = traverse(j, set())
            if temp:
                ans += 1
                master.update(temp)
        return ans

