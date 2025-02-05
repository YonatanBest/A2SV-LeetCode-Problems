# Problem: Check if All Characters Have Equal Number of Occurrences - https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/description/

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