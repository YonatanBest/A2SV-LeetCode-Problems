from collections import Counter
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        rep = Counter(s)
        x = 0
        check = True
        for i in rep:
            if check:
                check = False
                x = rep[i]
            if not (x == rep[i]):
                return False
        return True