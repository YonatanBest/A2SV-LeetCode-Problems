class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles.sort(reverse=True)
        for j in range(k):
            # print(piles)
            piles[0] -= piles[0]//2
            parent = 0
            
            while 2*parent + 2 < len(piles) and (piles[parent] < piles[2*parent + 1] or piles[parent] < piles[2*parent + 2]):
                if piles[2*parent + 1] < piles[2*parent + 2]:
                    piles[2*parent + 2], piles[parent] = piles[parent], piles[2*parent + 2]
                    parent = 2*parent + 2
                else:
                    piles[2*parent + 1], piles[parent] = piles[parent], piles[2*parent + 1]
                    parent = 2*parent + 1
                    
            while 2*parent + 1 < len(piles) and piles[parent] < piles[2*parent + 1]:
                    piles[2*parent + 1], piles[parent] = piles[parent], piles[2*parent + 1]
                    parent = 2*parent + 1
                    
        return sum(piles)
            
        