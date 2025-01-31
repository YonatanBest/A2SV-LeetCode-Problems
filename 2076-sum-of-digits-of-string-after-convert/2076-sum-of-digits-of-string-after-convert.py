class Solution:
    def getLucky(self, s: str, k: int) -> int:
        arr = []
        for i in s:
            arr.append(str(ord(i) - 96))
        total = "".join(arr)
        for i in range(k):
            temp = 0
            for j in total:
                temp += int(j)
            total = str(temp)
        return int(total)