class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        dic = Counter(s)
        arr = ["1"]*(dic["1"] - 1) + ["0"]*dic["0"] + ["1"]

        return "".join(arr)