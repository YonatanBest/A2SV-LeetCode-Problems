class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        count = 0
        visited = set()
        for f in fruits:
            for i in range(len(baskets)):
                if i not in visited and f <= baskets[i]:
                    visited.add(i)
                    break
            else:
                count += 1

        return count       