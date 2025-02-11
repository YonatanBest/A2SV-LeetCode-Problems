# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        ans = []
        i = 0
        j = len(piles) - 1
        count = 0
        while i <= j:
            if count == 2:
                ans.append(piles[j])
                j -= 1
                count = 0
            else:
                count += 1
                ans.append(piles[i])
                i += 1
        total = 0
        for i in range(len(ans)):
            if i % 3 == 1:
                total += ans[i]
        return total