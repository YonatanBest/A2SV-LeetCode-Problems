class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0 or n == 1:
            return bool(n)
        while n != 1:
            if n % 2 == 0:
                n //= 2
            if n % 3 == 0:
                n //= 3
            if n % 5 == 0:
                n //= 5
            if n % 2 and n % 3 and n % 5:
                break
        return n == 1