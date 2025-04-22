class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = []
        test = {}
        
        for i in range(len(equations)):
            if equations[i][0] not in test:
                test[equations[i][0]] = len(graph)
                graph.append([[equations[i][1], values[i]]])
            else:
                graph[test[equations[i][0]]].append([equations[i][1], values[i]])
                
            if equations[i][1] not in test and values[i]:
                test[equations[i][1]] = len(graph)
                graph.append([[equations[i][0], 1/values[i]]])
            elif values[i]:
                graph[test[equations[i][1]]].append([equations[i][0], 1/values[i]])

        def traverse(start, end, visited):
            if start not in test:
                return  -1 
                
            if end not in test:
                return -1 
                
            visited.add(start)
            
            if start == end:
                return 1
            
            for j in graph[test[start]]:   
                
                if j[0] not in visited:   
                    temp = traverse(j[0],end,visited)
                    
                    if temp != -1:
                        return j[1]*temp
            return -1
        
        
        ans = []
        for que in queries:
            ans.append(traverse(que[0], que[1], set()))
                
        return ans