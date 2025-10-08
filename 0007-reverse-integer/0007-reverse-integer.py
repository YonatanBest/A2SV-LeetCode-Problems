class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1
        x = sign * x
        reversed_num = 0
        while x:
            reversed_num *= 10
            reversed_num += x % 10
            x //= 10
            if reversed_num * sign < -2147483648 or reversed_num * sign > 2147483647:
                return 0
        return reversed_num * sign