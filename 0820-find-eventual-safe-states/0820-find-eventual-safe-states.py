class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # ans = []
        # def traverse(node, visited):
        #     if not graph[node]:
        #         return True
        #     for ele in graph[node]:
        #         if ele in visited:
        #             return False
        #         visited.add(ele)
        #         if not traverse(node, visited):
        #             return False
        #     return True

        # for j in range(len(graph)):
        #     if traverse(j, set([j])):
        #         ans.append(j)

        # return ans

        indeg = defaultdict(int)

        new_graph = defaultdict(list)

        n = len(graph)

        for node in range(n):
            for nei in graph[node]:
                new_graph[nei].append(node)

                indeg[node] += 1

        queue = deque()

        for node in range(n):
            if indeg[node] == 0:
                queue.append(node)

        order = []

        while queue:
            node = queue.popleft()

            order.append(node)

            for nei in new_graph[node]:

                indeg[nei] -= 1

                if indeg[nei] == 0:
                    queue.append(nei)

        return sorted(order)