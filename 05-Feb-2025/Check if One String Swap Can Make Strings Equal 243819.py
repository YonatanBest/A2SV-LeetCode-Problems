# Problem: Check if One String Swap Can Make Strings Equal - https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/description/

from collections import Counter
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        else:
            count = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    count += 1
            if count != 2:
                return False
            else:
                sd1 = Counter(s1)
                sd2 = Counter(s2)

                if sd1 == sd2:
                    return True
                else:
                    return False