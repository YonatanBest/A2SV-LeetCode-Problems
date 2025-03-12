# Problem: Factorial Trailing Zeroes - https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        def factorial(n):
            if n == 1 or n == 0:
                return 1

            return n*factorial(n-1)
        ans = factorial(n)
        count = 0
        while ans:
            if ans % 10 == 0:
                count += 1
                ans //= 10
            else:
                break
        return count


        