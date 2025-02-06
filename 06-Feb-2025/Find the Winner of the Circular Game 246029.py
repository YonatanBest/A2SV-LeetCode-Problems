# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = []
        for i in range(1, n + 1):
            arr.append(i)
        start = 0
        while len(arr) > 1:
            mod = (k - 1 + start) % (len(arr))
            arr.remove(arr[mod])
            start = mod
        return arr[0]