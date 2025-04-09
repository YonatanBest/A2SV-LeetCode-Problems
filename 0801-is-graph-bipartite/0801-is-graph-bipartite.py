class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def traverse(sender, i, state):
            if arr[i] == None:
                arr[i] = state
            elif arr[i] != state:
                return False
            else:
                return True

            for j in graph[i]:
                if sender == j:
                    continue
                if not traverse(i, j, not state):
                    return False
            return True
        
        for i in range(len(graph)):
            arr = [None]*len(graph)
            if not traverse(None, i, True):
                return False
        return True

