class Solution:
    def myPow(self, x: float, n: int) -> float:
        # if n == 0:
        #     return 1
        # if x == 0:
        #     return 0
        if abs(x) == 1:
            if n % 2:
                return x
            else:
                return 1
        if n < -2_000_000:
            return 0
        if n > 2_000_000 and x < 1:
            return 0
        
        flag = True if n < 0 else False
        n = abs(n)
        # rem = n % 500_000
        # num = n // 500_000
        # print(rem, num)
        # def power(x, n):
        #     if n == 0:
        #         return 1
        #     return x * power(x, n - 1)
        # ans = 1
        # if num > 0:
        #     ans = power(x, 500_000)
        #     ans = power(ans, num)
        # if rem > 0:
        #     ans *= power(x, rem)
        # return ans if not flag else 1/ans
        if x == 0:
            return 0
        if n == 0:
            return 1
        def power(x, n):
            if n == 1:
                return x
            if n == 0:
                return 1

            right = n//2
            left = n - right
            ans1 = power(x, right)
            ans2 = power(x, left)
            return ans1 * ans2
        ans = power(x, n)
        return ans if not flag else 1/ans

