class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: abs(x[0] - x[1]), reverse=True)
        num_city_a = 0
        num_city_b = 0
        min_sum = 0
        for cost in costs:
            if cost[0] < cost[1] and num_city_a < len(costs)//2:
                min_sum += cost[0]
                num_city_a += 1
            elif cost[0] > cost[1] and num_city_b < len(costs)//2:
                min_sum += cost[1]
                num_city_b += 1
            elif num_city_b >= len(costs)//2:
                min_sum += cost[0]
                num_city_a += 1
            else:
                min_sum += cost[1]
                num_city_b += 1
        return min_sum