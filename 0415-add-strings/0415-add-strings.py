class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = list(reversed(num1))
        num2 = list(reversed(num2))
        carry = 0
        i = 0
        ans = []
        while i < len(num1) and i < len(num2):
            new = int(num1[i]) + int(num2[i]) + carry
            ans.append(str(new%10))
            carry = new // 10
            i += 1
        while i < len(num1):
            new = int(num1[i]) + carry
            ans.append(str(new%10))
            carry = new // 10
            i += 1
        while i < len(num2):
            new = int(num2[i]) + carry
            ans.append(str(new%10))
            carry = new // 10
            i += 1
        if carry:
            ans.append(str(carry))
        ans = list(reversed(ans))

        return "".join(ans)