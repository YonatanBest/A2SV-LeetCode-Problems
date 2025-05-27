class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        ans = 0
        for j in range(1, n + 1):
            if j % m:
                ans += j
            else:
                ans -= j
        return ans