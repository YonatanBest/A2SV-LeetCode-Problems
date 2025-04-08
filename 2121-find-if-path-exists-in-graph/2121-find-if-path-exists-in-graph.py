class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        arr = [[] for i in range(n)]
        if not edges:
            return source == destination
        for i, j in edges:
            arr[i].append(j)
            arr[j].append(i)
        print(arr)
        def traverse(path, visited):
            if not path:
                return False
            for node in path:
                if node == destination:
                    return True
                if node not in visited:
                    visited.add(node)
                    if traverse(arr[node], visited):
                        return True
            return False
        return traverse(arr[source], set())