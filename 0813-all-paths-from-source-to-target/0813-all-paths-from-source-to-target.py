class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        all_paths = []

        def find_paths(path, candidates):

            if path[-1] == len(graph) - 1:
                all_paths.append(path.copy())
                return

            for can in candidates:
                path.append(can)
                find_paths(path, graph[can])
                path.pop()
            
            return

        find_paths([0], graph[0])

        return all_paths