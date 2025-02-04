from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        srep = Counter(s)
        trep = Counter(t)
        num = 0
        for i in srep:
            num += max(0, srep[i] - trep[i])
        return num