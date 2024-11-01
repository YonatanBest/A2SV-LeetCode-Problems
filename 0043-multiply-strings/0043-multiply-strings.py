class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num3 = 0
        num4 = 0
        for i in num1:
            num3 = num3 * 10
            num3 = num3 + ord(i) - 48
        for j in num2:
            num4 = num4 * 10
            num4 = num4 + ord(j) - 48
        return f"{num3*num4}"