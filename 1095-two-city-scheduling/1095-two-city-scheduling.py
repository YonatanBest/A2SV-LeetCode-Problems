class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0] - x[1])
        totalsum = 0
        for i in range(0, len(costs)//2):
            totalsum += costs[i][0]
        for i in range(len(costs)//2, len(costs)):
            totalsum += costs[i][1]
        return totalsum