import math
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        ans = math.log2(n)
        if ans % 2:
            return False
        else:
            return True
        