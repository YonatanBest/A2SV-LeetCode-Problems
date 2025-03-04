class Solution:
    def balancedStringSplit(self, s: str) -> int:
        dic = {"R":0, "L":0}
        count = 0
        for i in s:
            dic[i] += 1
            if dic["R"] == dic["L"]:
                count += 1
                dic = {"R":0, "L":0}
        return count