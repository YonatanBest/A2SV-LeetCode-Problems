# Problem: Pow (x, n) - https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if x == 0:
            return 0
        flag = True if n < 0 else False
        n = abs(n)
        rem = n % 500_000
        num = n // 500_000
        print(rem, num)
        def power(x, n):
            if n == 0:
                return 1
            return x * power(x, n - 1)
        ans = 1
        if num > 0:
            ans = power(x, 500_000)
            ans = power(ans, num)
        if rem > 0:
            ans *= power(x, rem)
        return ans if not flag else 1/ans
