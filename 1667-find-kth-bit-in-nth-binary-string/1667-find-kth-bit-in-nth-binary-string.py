class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        invert = {"0":"1", "1":"0"}
        ans = ["0"]
        def inverter(x):
            new = []
            for i in x:
                new.append(invert[i])
            new.reverse()
            return new
        def binaryString(n, ans):
            if n == 0:
                return ans
            ans.extend(["1"] + inverter(ans))
            binaryString(n-1, ans)
        binaryString(n, ans)
        return ans[k - 1]
