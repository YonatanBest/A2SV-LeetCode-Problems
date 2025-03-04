class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count = 0
        while target - 1:
            if maxDoubles and target % 2 == 0:
                target //= 2
                maxDoubles -= 1
            else:
                if not maxDoubles:
                    return count + target - 1
                target -= 1
            count += 1
        return count