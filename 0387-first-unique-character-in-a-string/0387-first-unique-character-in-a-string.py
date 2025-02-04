from collections import Counter, defaultdict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        rep = Counter(s)
        for i in rep:
            if rep[i] == 1:
                return s.index(i)
        return -1