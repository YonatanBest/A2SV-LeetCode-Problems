class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        ans = []
        sign = 1
        for j in range(len(x) - 1, -1, -1):
            if x[j].isdigit():
                ans.append(x[j])
            else:
                sign = -1

        ans = int("".join(ans)) * sign
        if ans >= -2147483648 and ans <= 2147483647:
            return ans
        return 0